import paho.mqtt.client as mqtt
import asyncio
import queue
import Constant.constant as const
from Cache.GlobalVariables import GlobalVariables
import logging
import threading
import socket
from Contracts.ITransport import ITransport

# added by cungdd 23/10
import re
import uuid
from base64 import b64encode
from Crypto.Cipher import AES

# def get_pwd():
#     import re
#     import uuid
#     from base64 import b64encode
#     from Crypto.Cipher import AES

#     BLOCK_SIZE = 16  # Bytes
#     pad = lambda s: s + (BLOCK_SIZE - len(s) % BLOCK_SIZE) * \
#                     chr(BLOCK_SIZE - len(s) % BLOCK_SIZE)
#     unpad = lambda s: s[:-ord(s[len(s) - 1:])]


#     mac = ''.join(re.findall('..', '%012x' % uuid.getnode()))
#     print(mac)
#     plaintext = '2804' + mac
#     print(plaintext)

#     key = 'RANGDONGRALSMART'
#     cipher = AES.new(key.encode('utf8'), AES.MODE_ECB)
#     plaintext = pad(plaintext)
#     cyphertext = b64encode(cipher.encrypt(plaintext.encode('utf-8')))
#     pwd = cyphertext.decode('utf-8')
#     print(pwd)
#     return pwd

# end
class MqttConfig:
    host: str
    port: int
    qos: int
    keep_alive: int
    username: str
    # password: str

    def __init__(self):
        hostname = socket.gethostname()
        ip = socket.gethostbyname(hostname)
        self.host = ip
        self.port = const.MQTT_PORT
        self.qos = const.MQTT_QOS
        self.keep_alive = const.MQTT_KEEPALIVE
        self.username = const.MQTT_USER
        self.password = const.MQTT_PASS

class Mqtt(ITransport):
    __mqttConfig: MqttConfig
    __client: mqtt.Client
    __globalVariables: GlobalVariables
    __logger: logging.Logger
    __lock: threading.Lock

    def __init__(self, log: logging.Logger):
        super().__init__()
        self.__logger = log
        self.__mqttConfig = MqttConfig()
        self.__client = mqtt.Client()
        self.__globalVariables = GlobalVariables()
        self.__lock = threading.Lock()

    def __on_message(self, client, userdata, msg):
        message = msg.payload.decode("utf-8")
        topic = msg.topic
        item = {"topic": topic, "msg": message}
        with self.__lock:
            self.receive_data_queue.put(item)
        return

    def __on_connect(self, client, userdata, flags, rc):
        self.__client.subscribe(topic=const.MQTT_RESPONSE_TOPIC, qos=self.__mqttConfig.qos)
        self.__client.subscribe(topic=const.MQTT_CONTROL_TOPIC, qos=self.__mqttConfig.qos)

    def send(self, destination, send_data):
        self.__client.publish(destination, payload=send_data, qos=const.MQTT_QOS)

    def disconnect(self):
        self.__client.disconnect()

    def connect(self):
        self.__client.on_message = self.__on_message
        self.__client.on_connect = self.__on_connect
        self.__client.username_pw_set(username=self.__mqttConfig.username, password=self.__mqttConfig.password)
        try:
            self.__client.connect(self.__mqttConfig.host, self.__mqttConfig.port)
            self.__client.loop_start()
        except Exception as err:
            self.__logger.error(f"Exception in connect to mqtt: {err}")
            print(f"Exception in connect to mqtt: {err}")

    def reconnect(self):
        pass

    def receive(self):
        pass
