from HcServices.Http import Http
import asyncio
from Database.Db import Db
from Cache.GlobalVariables import GlobalVariables
import datetime
import logging
import threading
from Contracts.ITransport import ITransport
from Helper.System import System, eliminate_current_progress, ping_google, check_and_kill_all_repeat_progress
from Contracts.IHandler import IHandler
from Helper.Terminal import execute_with_result, execute
import Constant.constant as Const


current_weather = {}

class RdHc:
    __httpServices: Http
    __signalServices: ITransport
    __mqttServices: ITransport
    __globalVariables: GlobalVariables
    __lock: threading.Lock
    __logger: logging.Logger
    __mqttHandler: IHandler
    __signalrHandler: IHandler

    def __init__(self, log: logging.Logger, http: Http, signalr: ITransport, mqtt: ITransport,
                 mqtt_handler: IHandler, signalr_handler: IHandler):
        self.__logger = log
        self.__httpServices = http
        self.__signalServices = signalr
        self.__mqttServices = mqtt
        self.__globalVariables = GlobalVariables()
        self.__lock = threading.Lock()
        self.__mqttHandler = mqtt_handler
        self.__signalrHandler = signalr_handler

    # time between 2 consecutive pings is 10s
    # google disconnect consecutive times max is 3
    async def __hc_check_connect_with_internet(self):
        ping_waiting_time = 10
        google_disconnect_count = 0
        first_success_ping_to_google_flag = False
        google_disconnect_count_limited = 4

        while True:
            self.__globalVariables.PingGoogleSuccessFlag = ping_google()

            if not self.__globalVariables.PingGoogleSuccessFlag:
                google_disconnect_count = google_disconnect_count + 1
            if self.__globalVariables.PingGoogleSuccessFlag:
                first_success_ping_to_google_flag = True
                google_disconnect_count = 0
            if google_disconnect_count == google_disconnect_count_limited:
                self.__hc_update_disconnect_status_to_db()
                if first_success_ping_to_google_flag:
                    eliminate_current_progress()
            await asyncio.sleep(ping_waiting_time)

    # time between 2 consecutive pings is 60s(FPT requirement)
    # this time is detached: first 5s, second 55s(because of waiting to ping google)
    # cloud disconnect consecutive times max is 3(FPT requirement)
    async def __hc_check_connect_with_cloud(self):
        s = System(self.__logger)
        signalr_disconnect_count = 0
        first_success_ping_to_cloud_flag = False
        signalr_disconnect_count_limit = 3

        while True:
            print("Hc send heartbeat to cloud")
            self.__logger.info("Hc send heartbeat to cloud")

            await asyncio.sleep(5)

            if self.__globalVariables.DisconnectTime is None:
                self.__globalVariables.DisconnectTime = datetime.datetime.now()

            if not self.__globalVariables.PingGoogleSuccessFlag:
                self.__globalVariables.PingCloudSuccessFlag = False
            if self.__globalVariables.PingGoogleSuccessFlag:
                self.__globalVariables.PingCloudSuccessFlag = \
                    await s.send_http_request_to_heartbeat_url(self.__httpServices)

            if not self.__globalVariables.PingCloudSuccessFlag:
                print("can not ping to cloud")
                self.__logger.info("can not ping to cloud")
                signalr_disconnect_count = signalr_disconnect_count + 1
                self.__globalVariables.SignalrConnectSuccessFlag = False

            if self.__globalVariables.PingCloudSuccessFlag:
                await s.recheck_reconnect_status_of_last_activation()
                if not first_success_ping_to_cloud_flag:
                    first_success_ping_to_cloud_flag = True
                self.__globalVariables.DisconnectTime = None
                signalr_disconnect_count = 0

            if (signalr_disconnect_count == signalr_disconnect_count_limit) \
                    and (not self.__globalVariables.SignalrDisconnectStatusUpdateFlag):
                self.__hc_update_disconnect_status_to_db()
                if first_success_ping_to_cloud_flag:
                    self.__logger.info("program had been eliminated")
                    print("program had been eliminated")
                    eliminate_current_progress()
                    
            await asyncio.sleep(55)

    async def __hc_update_reconnect_status_to_db(self):
        self.__logger.info("Update cloud reconnect status to db")
        print("Update cloud reconnect status to db")
        s = System(self.__logger)
        await s.update_reconnect_status_to_db(datetime.datetime.now())

    def __hc_update_disconnect_status_to_db(self):
        self.__logger.info("Update cloud disconnect status to db")
        print("Update cloud disconnect status to db")
        s = System(self.__logger)
        s.update_disconnect_status_to_db(self.__globalVariables.DisconnectTime)

    async def __hc_handler_mqtt_data(self):
        mqtt_handler_delay_time = 1
        while True:
            await asyncio.sleep(mqtt_handler_delay_time)
            if not self.__mqttServices.receive_data_queue.empty():
                with self.__lock:
                    item = self.__mqttServices.receive_data_queue.get()
                    self.__mqttHandler.handler(item)
                    self.__mqttServices.receive_data_queue.task_done()

    async def __hc_handler_signalr_data(self):
        signalr_handler_delay_time = 1
        while True:
            await asyncio.sleep(signalr_handler_delay_time)
            if not self.__signalServices.receive_data_queue.empty():
                with self.__lock:
                    item = self.__signalServices.receive_data_queue.get()
                    self.__signalrHandler.handler(item)
                    self.__signalServices.receive_data_queue.task_done()

    # report time interval is 1800(FPT requirements)
    async def __hc_report_online_status_to_cloud(self):
        report_time_interval = 1800
        s = System(self.__logger)
        while True:
            await asyncio.sleep(1)
            if self.__globalVariables.PingCloudSuccessFlag and not self.__globalVariables.AllowChangeCloudAccountFlag:
                await s.send_http_request_to_gw_online_status_url(self.__httpServices)
                await asyncio.sleep(report_time_interval)

    def __hc_get_gateway_mac(self):
        s = System(self.__logger)
        s.get_gateway_mac()

    #load refresh token and dormitoryId from db in runtime
    def __hc_load_user_data(self):
        db = Db()
        user_data = db.Services.UserdataServices.FindUserDataById(id=1)
        dt = user_data.first()
        if dt is not None:
            self.__globalVariables.DormitoryId = dt["DormitoryId"]
            self.__globalVariables.RefreshToken = dt["RefreshToken"]
            self.__globalVariables.AllowChangeCloudAccountFlag = dt["AllowChangeAccount"]

    #load current wifi SSID
    def __hc_load_current_wifi_name(self):
        s = System(self.__logger)
        s.update_current_wifi_name()


    
    #checking when wifi is changed
    async def __hc_check_wifi_change(self):
        s = System(self.__logger)
        checking_waiting_time = 10
        while True:
            await asyncio.sleep(checking_waiting_time)
            await s.check_wifi_change(self.__signalServices)
    
    # added by cungdd 16/10
    async def __hc_update_weather_status(self):
        import requests
        import json
        
        global current_weather
        db = Db()
        user_data = db.Services.UserdataServices.FindUserDataById(id=1)
        dt = user_data.first()
        if dt is not None:
            lat = dt['Latitude']
            lon = dt["Longitude"]

        api_key = "05f40f1972e5ae4ff4fa2bbe2bd9adae"
        url = "https://api.openweathermap.org/data/2.5/onecall?lat=%s&lon=%s&appid=%s&units=metric" % (lat, lon, api_key)

        while True:
            try:
                response = requests.get(url)
                data = json.loads(response.text)
                weather = data['current']['weather'][0]
                cmd = {"cmd":"outWeather"}
                weather.update(cmd)
                temp = {"temp": data['current']['temp']}
                weather.update(temp)
                humi = {"humi": data['current']['humidity']}
                weather.update(humi)
            
                current_weather = weather
                self.__mqttServices.send(
                    Const.MQTT_CONTROL_TOPIC, json.dumps(current_weather))
                self.__logger.info("\n--------->>>>>>>> UPDATE OUT WEATHER <<<<<<<<----------\n")
            except:
                self.__mqttServices.send(
                    Const.MQTT_CONTROL_TOPIC, json.dumps(current_weather))
            await asyncio.sleep(Const.HC_UPDATE_WEATHER_INTERVAL)
        
    # end


    # added by cungdd 21/10
    async def __hc_check_service_status(self):
        import subprocess
        import os

        while True:
            count_service = 0

            process = subprocess.Popen(['pgrep', 'SYSTEM'],
                           stdout=subprocess.PIPE,
                           universal_newlines=True)
            output_1 = process.stdout.readlines()
            for line in output_1:
                count_service += 1
                print('\nSYSTEM service is running')

            process = subprocess.Popen(['pgrep', 'RD_SMART'],
                           stdout=subprocess.PIPE,
                           universal_newlines=True)
            output_2 = process.stdout.readlines()
            for line in output_2:
                count_service += 1
                print('\nRD_SMART service is running')

            output_3 = os.popen('ps | grep "python3 RDhcPy/main.py" | grep -v "grep" | wc -l').read().strip()

            if output_3 == '1':
                count_service += 1
                print('\npython3 RDhcPy/main.py service is running\n')
                
            if count_service == 3:
                os.system('/bin/echo "1" > /sys/class/leds/linkit-smart-7688:orange:service/brightness')
            else:
                print("Service fail !!!\n")
                os.system('/bin/echo "0" > /sys/class/leds/linkit-smart-7688:orange:service/brightness')

            await asyncio.sleep(Const.HC_CHECK_SERVICE_INTERVAL)

    
    
    async def __hc_send_version_info(self):
        s = System(self.__logger)
        await s.update_firmware_version_info_to_cloud(self.__httpServices)



    async def run(self):
        check_and_kill_all_repeat_progress()
        self.__hc_get_gateway_mac()
        self.__hc_load_user_data()
        self.__hc_load_current_wifi_name()
        self.__mqttServices.connect()
        task0 = asyncio.create_task(self.__signalServices.connect())
        task1 = asyncio.create_task(self.__hc_handler_signalr_data())
        task2 = asyncio.create_task(self.__hc_check_connect_with_cloud())
        task3 = asyncio.create_task(self.__hc_handler_mqtt_data())
        task4 = asyncio.create_task(self.__hc_check_connect_with_internet())
        task5 = asyncio.create_task(self.__hc_check_wifi_change())
        task6 = asyncio.create_task(self.__hc_report_online_status_to_cloud())
        task7 = asyncio.create_task(self.__hc_update_weather_status())
        task8 = asyncio.create_task(self.__hc_check_service_status())
        task9 = asyncio.create_task(self.__hc_send_version_info())
        tasks = [task0, task1, task2, task3, task4, task5, task6, task7, task8, task9]
        await asyncio.gather(*tasks)
