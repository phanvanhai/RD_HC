from Contracts.IHandler import IHandler
import asyncio
import logging
from Contracts.ITransport import ITransport
from Cache.GlobalVariables import GlobalVariables
import Constant.constant as const
import json
from Database.Db import Db
from Model.userData import userData
from Helper.System import System, ping_google

from Handler.TuyaAPIHandler import TuyaAPI

import sqlite3


def sql_update(cmd):
    con = sqlite3.connect('rd.Sqlite')
    cur = con.cursor()
    cur.execute(cmd)
    con.commit()
    con.close()


tokenTime = 0

#   ==============================================================================================

class MqttDataHandler(IHandler):
    __logger: logging.Logger
    __mqtt: ITransport
    __signalr: ITransport
    __globalVariables: GlobalVariables
    __tuyaAPI: TuyaAPI

    def __init__(self, log: logging.Logger, mqtt: ITransport, signalr: ITransport):
        self.__logger = log
        self.__mqtt = mqtt
        self.__globalVariables = GlobalVariables()
        self.__signalr = signalr

    def handler(self, item):
        topic = item['topic']
        message = item['msg']
        switcher = {
            const.MQTT_RESPONSE_TOPIC: self.__handler_topic_hc_control_response,
            const.MQTT_CONTROL_TOPIC: self.__handler_topic_hc_control,
        }
        func = switcher.get(topic)
        func(message)
        return

    def __handler_topic_hc_control_response(self, data):
        if self.__globalVariables.AllowChangeCloudAccountFlag:
            return
        print("data from topic HC.CONTROL.RESPONSE: " + data)
        self.__logger.debug("data from topic HC.CONTROL.RESPONSE: " + data)

        if self.__globalVariables.PingCloudSuccessFlag:

            try:
                json_data = json.loads(data)
                cmd = json_data.get("CMD", "")
                dt = json_data.get("DATA", "")

                self.__hc_check_cmd_and_send_response_to_cloud(cmd, data)

                switcher = {
                    "DEVICE": self.__handler_cmd_device
                }
                func = switcher.get(cmd)
                func(dt)

            except:
                self.__logger.error("mqtt data receiver in topic HC.CONTROL.RESPONSE invalid")

    def __handler_topic_hc_control(self, data):
        print("data from topic HC.CONTROL: \n" + data)
        self.__logger.debug("data from topic HC.CONTROL: " + data)

        try:
            json_data = json.loads(data)
            cmd = json_data.get("CMD", "")
            dt = json_data.get("DATA", "")
            switcher = {
                "HC_CONNECT_TO_CLOUD": self.__handler_cmd_hc_connect_to_cloud,
                "RESET_HC": self.__handler_cmd_reset_hc,
                "UPDATE_FIRMWARE": self.__handler_cmd_update_firmware,
                "TUYA_CONTROL": self.__handler_cmd_tuya_control,
                "DEVICE_UPDATE": self.__handler_cmd_tuya_device_update
            }
            func = switcher.get(cmd)
            func(dt)
        except:
            self.__logger.error("mqtt data receiver in topic HC.CONTROL invalid")

    def __handler_cmd_tuya_device_update(self, data):
        device_id = data.get('DEVICE_ID')
        access_id = data.get('ACCESS_ID')
        access_key = data.get('ACCESS_KEY')
        self.__tuyaAPI = TuyaAPI('https://openapi.tuyaus.com', access_id, access_key, device_id)
        self.__tuyaAPI.GetAccessToken()
        self.__tuyaAPI.GetDeviceStatus()

    def __handler_cmd_tuya_control(self, data):
        network_id = data.get('TUYA_NETWORK_ID')
        switcher = {
            0 : self.__handler_cmd_tuya_ble_device,
            1 : self.__handler_cmd_tuya_wifi_device,
            2 : self.__handler_cmd_tuya_ir_device
        }
        func = switcher.get(network_id)
        func(data)

    def __handler_cmd_tuya_wifi_device(self, data):
        device_id = data.get('DEVICE_ID')
        access_id = data.get('ACCESS_ID')
        access_key = data.get('ACCESS_KEY')
        self.__tuyaAPI = TuyaAPI('https://openapi.tuyaus.com', access_id, access_key, device_id)
        type_id = data.get('TYPE_ID')
        if type_id == 0:
            code = "switch_1"
        elif type_id == 1:
            code = "switch_led"
        properties = data.get('PROPERTIES', [])
        # print(properties)
        for property in properties:
            if property.get('ID') == 0:
                commands = {
                    "code":code,
                    "value": bool(property.get('VALUE'))
                }
                self.__tuyaAPI.GetAccessToken()
                self.__tuyaAPI.device_control(commands)
            elif property.get('ID') == 1:
                commands = {
                    "code":"bright_value",
                    "value": property.get('VALUE')
                }
                self.__tuyaAPI.GetAccessToken()
                self.__tuyaAPI.device_control(commands)
            elif property.get('ID') == 2:
                commands = {
                    "code":"temp_value",
                    "value": property.get('VALUE')
                }
                self.__tuyaAPI.GetAccessToken()
                self.__tuyaAPI.device_control(commands)
            elif property.get('ID') == 3:
                commands = {
                    "code":"colour_data",
                    "value": property.get('VALUE')
                }
                self.__tuyaAPI.GetAccessToken()
                self.__tuyaAPI.device_control(commands)

    def __handler_cmd_tuya_ble_device(self, data):
        pass

    # added by cungdd 25/10
    def __handler_cmd_tuya_ir_device(self, data):
        INFRARED_ID = 'eb1604e7309a2b7793e7ut'
        REMOTE_AIR_ID = 'eb36df2c1ff4040648zl4s'
        REMOTE_TV_ID = 'ebefd065ee2ce5250fa3ao'
        commands = {
            "code":data.get("code"),
            "value": data.get("value")
        }
        self.__tuyaAPI.GetAccessToken()
        print(commands)
        if data.get("typdev") == "AIR_CONDITIONER":
            self.__tuyaAPI.IR_AirConditionControl(INFRARED_ID, REMOTE_AIR_ID, 1, 2, 27, 3, commands)
        elif data.get("typdev") == "TV":
            self.__tuyaAPI.IR_TVControlOnOff(INFRARED_ID, REMOTE_TV_ID)

    # added by cungdd 29/10
    def __handler_cmd_update_firmware(self, data):
        import subprocess
        import os
        import time

        print("Start update firmware ...")
        try:
            os.system('opkg update')
            os.system('pip3 install packaging')
            os.system('opkg update')
            os.system('opkg upgrade tar')
            file = open("/etc/version.txt", "r")
            current_ver = file.read().strip()
            print(f"Current version: {current_ver}")
            file.close()
            from packaging import version

            lastest_ver = data[-1]
            print(lastest_ver)
            lastest_ver_name = lastest_ver.get('NAME')
            print(lastest_ver_name)

            if version.parse(lastest_ver_name) > version.parse(current_ver):
                link = lastest_ver.get('URL')
                file_name = link[link.rfind('/')+1:]
                link_dl = "wget " + "https://iot-dev.truesight.asia" + link
                os.system(link_dl)

                process = subprocess.Popen(['sha256sum', f'{file_name}'],
                                            stdout=subprocess.PIPE,
                                            universal_newlines=True)
                output = process.stdout.readline()
                src = output.strip()
                check_sum = lastest_ver.get('CHECK_SUM') + "  " + file_name
                if src == check_sum:
                    os.system(f'tar -xf {file_name}')

                    # move old file to dir /etc/RECOVERY
                    os.system('mv RDhcPy/ /etc/RECOVERY')
                    os.system('mv *.ipk /etc/RECOVERY')
                    os.system('mv version.txt /etc/RECOVERY')
                    os.system(f'rm {file_name}')

                    # move new file to dir root
                    os.system(f'mv /root/{lastest_ver_name}/* /root/')
                    os.system(f'rm -r {lastest_ver_name}/')

                    # handle condition version required

                    file = open("version.txt", "r")
                    str_ver = file.read().strip()
                    list_vers = str_ver.split('-')
                    print(list_vers)
                    file.close()

                    # required list version
                    req_list_vers = [] 
                    for ver in list_vers:
                        if version.parse(ver) > version.parse(current_ver):
                            req_list_vers.append(ver)
                    print(req_list_vers)

                    for req_ver in req_list_vers:
                        for d in data:
                            if req_ver == d.get('NAME'):
                                # if req_ver == lastest_ver_name:
                                #     print("Pass")
                                # else:
                                link_sub = d.get('URL')
                                file_sub_name = link_sub[link_sub.rfind('/')+1:]
                                link_sub_dl = "wget " + "https://iot-dev.truesight.asia" + link_sub
                                os.system(link_sub_dl)

                                process = subprocess.Popen(['sha256sum', f'{file_sub_name}'],
                                                            stdout=subprocess.PIPE,
                                                            universal_newlines=True)
                                output = process.stdout.readline()
                                src = output.strip()
                                print(src)
                                check_sum = d.get('CHECK_SUM') + "  " + file_sub_name
                                print(check_sum)
                                if src == check_sum:
                                    print("Start install sub-version")
                                    os.system(f'tar -xf {file_sub_name}')

                                    # move old file to dir /etc/RECOVERY
                                    os.system('rm -r /etc/RECOVERY/*')
                                    os.system('mv RDhcPy/ /etc/RECOVERY')
                                    os.system('mv *.ipk /etc/RECOVERY')
                                    os.system('mv version.txt /etc/RECOVERY')
                                    os.system(f'rm {file_sub_name}')

                                    # move new file to dir root
                                    os.system(f'mv /root/{req_ver}/* /root/')
                                    os.system(f'rm -r {req_ver}/')

                                    # install new file
                                    os.system('opkg install *.ipk')

                                    # delete /etc/RECOVERY
                                    os.system('rm -r /etc/RECOVERY/*')

                                    file = open("/etc/version.txt", "w")
                                    file.write(req_ver)
                                    file.close()


                    # install new file
                    # os.system('opkg install *.ipk')

                    # # delete /etc/RECOVERY
                    # os.system('rm -r /etc/RECOVERY/*')

                    # file = open("/etc/version.txt", "w")
                    # file.write(lastest_ver_name)
                    # file.close()
                    time.sleep(4)
                    os.system('reboot -f')
        except:
            print("Update firmware error !")

    
    # end


    def __handler_cmd_device(self, data):
        if self.__globalVariables.AllowChangeCloudAccountFlag:
            return
        signal_data = []
        try:
            for d in data:
                for i in d["PROPERTIES"]:
                    data_send_to_cloud = {
                        "deviceId": d['DEVICE_ID'],
                        "deviceAttributeId": i['ID'],
                        "value": i['VALUE']
                    }
                    signal_data.append(data_send_to_cloud)
        except:
            self.__logger.debug("data of cmd Device invalid")
            print("data of cmd Device invalid")

        if signal_data:
            send_data = [const.SIGNALR_CLOUD_RESPONSE_ENTITY, json.dumps(signal_data)]
            self.__signalr.send(self.__globalVariables.DormitoryId, send_data)

        if not signal_data:
            self.__logger.debug("have no data to send to cloud via signalr")
            print("have no data to send to cloud via signalr")
    

    def __handler_cmd_hc_connect_to_cloud(self, data):
        db = Db()
        dormitory_id = data.get("DORMITORY_ID", "")
        refresh_token = data.get("REFRESH_TOKEN", "")
        longitude = data.get('LONGITUDE')
        latitude = data.get('LATITUDE')

        if not self.__globalVariables.AllowChangeCloudAccountFlag and self.__globalVariables.DormitoryId != "":
            return

        if refresh_token != "":
            self.__globalVariables.RefreshToken = refresh_token
        self.__globalVariables.DormitoryId = dormitory_id

        self.__globalVariables.AllowChangeCloudAccountFlag = False

        user_data = userData(refreshToken=refresh_token, dormitoryId=dormitory_id, allowChangeAccount=False)
        rel = db.Services.UserdataServices.FindUserDataById(id=1)
        dt = rel.first()
        if dt is not None:
            db.Services.UserdataServices.UpdateUserDataById(id=1, newUserData=user_data)
            cmd = "UPDATE UserData SET Longitude = " + str(longitude) + ", Latitude = " + str(latitude) + " WHERE Id = 1 "
            sql_update(cmd)
        if dt is None:
            db.Services.UserdataServices.AddNewUserData(newUserData=user_data)
            cmd = "UPDATE UserData SET Longitude = " + str(longitude) + ", Latitude = " + str(latitude) + " WHERE Id = 1 "
            sql_update(cmd)
            return

    def __handler_cmd_reset_hc(self, data):
        print("Allow to change account, now new account can log in")
        self.__logger.info("Allow to change account, now new account can log in")

        db = Db()
        self.__globalVariables.AllowChangeCloudAccountFlag = True

        rel = db.Services.UserdataServices.FindUserDataById(id=1)
        dt = rel.first()
        if dt is None:
            return

        user_data = userData(refreshToken=self.__globalVariables.RefreshToken,
                             dormitoryId=self.__globalVariables.DormitoryId,
                             allowChangeAccount=self.__globalVariables.AllowChangeCloudAccountFlag)

        db.Services.UserdataServices.UpdateUserDataById(id=1, newUserData=user_data)

    def __hc_check_cmd_and_send_response_to_cloud(self, cmd: str, data: str):
        room_response_cmd = ["CREATE_ROOM", "ADD_DEVICE_TO_ROOM", "REMOVE_DEVICE_FROM_ROOM"]
        scene_response_cmd = ["CREATE_SCENE", "EDIT_SCENE"]
        if room_response_cmd.count(cmd) > 0:
            send_data = [const.SIGNALR_APP_ROOM_RESPONSE_ENTITY, data]
            self.__signalr.send(self.__globalVariables.DormitoryId, send_data)
            return

        if scene_response_cmd.count(cmd) > 0:
            send_data = [const.SIGNALR_APP_SCENE_RESPONSE_ENTITY, data]
            self.__signalr.send(self.__globalVariables.DormitoryId, send_data)
            return

        if (room_response_cmd + scene_response_cmd).count(cmd) == 0:
            send_data = [const.SIGNALR_APP_DEVICE_RESPONSE_ENTITY, data]
            self.__signalr.send(self.__globalVariables.DormitoryId, send_data)
            return
