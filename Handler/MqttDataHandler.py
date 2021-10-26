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


import hmac
import hashlib
import time
import requests
import json

tokenTime = 0

class TuyaAPI():
    def __init__(self):
        self.__base = 'https://openapi.tuyaus.com'
        self.__client_id = 'kypn3s89aytjc0hwth6v'
        self.__secret = 'ef60ffa003564c78aaab6d75111ea367'

    def stringToSignGetKey(self, msg, header, url):
        msgA = bytes(msg, 'utf-8')
        signURL = 'GET' + '\n' + hashlib.sha256(msgA).hexdigest() + '\n' + header + '\n' + url
        return signURL


    def stringToSignPOST(self, msg, header, url):
        msgA = bytes(msg, 'utf-8')
        signURL = 'POST' + '\n' + hashlib.sha256(msgA).hexdigest() + '\n' + header + '\n' + url
        return signURL
        

    def calc_sign(self, msg, key):
        sign = hmac.new(msg=bytes(msg, 'latin-1'),key = bytes(key, 'latin-1'), digestmod = hashlib.sha256).hexdigest().upper()
        return sign


    def GetAccessToken(self):
        global tokenTime
        tokenTime = tokenTime + 1
        t = str(int(time.time()*1000))
        urlGetToken = '/v1.0/token?grant_type=1'
        r = requests.get(self.__base + urlGetToken,
                        headers={
                            'client_id':self.__client_id,
                            'sign':self.calc_sign(self.__client_id + t + self.stringToSignGetKey('','',urlGetToken), self.__secret),
                            'secret': self.__secret,
                            't':t,
                            'sign_method':'HMAC-SHA256',
                            })
        if(r.json()['success'] == True):
            global res
            res = r.json()['result']
            #print('success data:' + str(res))
        else:
            print('Can not get Token')
        return r.json()['success']


    def POST(self, url, headers={}, body={}):
        import json
        t = str(int(time.time()*1000))

        default_par={
            'client_id':self.__client_id,
            'access_token':res['access_token'],
            'sign':self.calc_sign(self.__client_id+res['access_token'] + t + self.stringToSignPOST(json.dumps(body), '', url), self.__secret),
            't':t,
            'sign_method':'HMAC-SHA256'
            }
        r = requests.post(self.__base + url, headers=dict(default_par,**headers), data=json.dumps(body))
        r = json.dumps(r.json(), indent=2, ensure_ascii=False) # Beautify the request result format for easy printing and viewing
        return r


    def IR_TVControlOnOff(self, IR_ID, TV_ID):
        d = {"key": "Power"}
        r = self.POST(url = '/v1.0/infrareds/' + IR_ID + '/remotes/' + TV_ID +'/command', body=d)
        return(r)


    def IR_AirConditionControl(self, IR_ID, remote_id, power, mode, temp, wind, d):
        print("Control Air Conditioner Remote")
        r = self.POST(url = '/v1.0/infrareds/' + IR_ID + '/air-conditioners/' + remote_id +'/command', body=d)
        print(r)


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
        self.__tuyaAPI = TuyaAPI()

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
                    "DEVICE": self.__handler_cmd_device,
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
                "IR_CONTROL": self.__handler_cmd_ir_control
            }
            func = switcher.get(cmd)
            func(dt)
        except:
            self.__logger.error("mqtt data receiver in topic HC.CONTROL invalid")


    # added by cungdd 25/10
    def __handler_cmd_ir_control(self, data):
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

    # added by cungdd 20/10
    def __handler_cmd_update_firmware(self, data):
        import subprocess
        import os
        import time

        print("Start update firmware ...")
        os.system('rm *.tar.xz')
        link = data.get("link")
        link_dl = "wget " + link 
        print(link)
        print(link_dl)
        try:
            os.system(link_dl)

            process = subprocess.Popen(['sha256sum', 'test21102021.tar.xz'],
                                    stdout=subprocess.PIPE,
                                    universal_newlines=True)
            output = process.stdout.readline()
            src = output.strip()
            f = open("abc.txt", "r")
            ext = f.read().strip()
            if(src == ext):
                print("Update firmware processing...")

                # extract file
                os.system('tar -xf test21102021.tar.xz')
                # print("20%")

                # move old file to dir RECOVERY
                os.system('rm -r RECOVERY/*')
                os.system('mv RDhcPy/ RECOVERY')
                os.system('mv *.ipk RECOVERY')
                os.system('rm test21102021.tar.xz')
                # print("50%")

                # move new file to dir root
                os.system('mv /root/test21102021/* /root/')
                os.system('rm -r test21102021/')
                # print("70%")
                # time.sleep(5)

                # install new file
                os.system('opkg install *.ipk')

                # delete RECOVERY
                os.system('rm -r RECOVERY/*')
                # print("100%")

                print("Update firmware finished. HC will reboot now")
                time.sleep(2)
                            
                os.system('reboot -f')
            else:
                print("Update firmware error")
        except:
            print("Download error !")
            self.__logger.info("Download error !")
            pass
    
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
        if dt is None:
            db.Services.UserdataServices.AddNewUserData(newUserData=user_data)
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
