import hmac
import hashlib
import time
import requests
import json


class TuyaAPI():
    def __init__(self, base, client_id, secret, device_id):
        self.__base = base
        self.__client_id = client_id
        self.__secret = secret
        self.__device_id = device_id

    def stringToSignGetKey(self, msg, header, url):
        msgA = bytes(msg, 'utf-8')
        signURL = 'GET' + '\n' + hashlib.sha256(msgA).hexdigest() + '\n' + header + '\n' + url
        return signURL

    def stringToSignPOST(self, msg, header, url):
        msgA = bytes(msg, 'utf-8')
        signURL = 'POST' + '\n' + hashlib.sha256(msgA).hexdigest() + '\n' + header + '\n' + url
        return signURL        

    def stringToSignGET(self, msg, header, url):
        msgA = bytes(msg, 'utf-8')
        signURL = 'GET' + '\n' + hashlib.sha256(msgA).hexdigest() + '\n' + header + '\n' + url
        return signURL

    def calc_sign(self, msg, key):
        sign = hmac.new(msg=bytes(msg, 'latin-1'),key = bytes(key, 'latin-1'), digestmod = hashlib.sha256).hexdigest().upper()
        return sign

    def GetAccessToken(self):
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

    def GET(self, url, headers={}):
        t = str(int(time.time()*1000))
        default_par={
            'client_id': self.__client_id,
            'access_token':res['access_token'],
            'sign': self.calc_sign(self.__client_id+res['access_token']+t + self.stringToSignGET('','',url), self.__secret),
            't':t,
            'sign_method':'HMAC-SHA256',  
            }
        r = requests.get(self.__base + url, headers=dict(default_par,**headers))
        r = json.dumps(r.json(), indent=2, ensure_ascii=False) # Beautify the request result format for easy printing and viewing
        return r

    def PUT(self, url, headers={}, body={}):
        import json
        t = str(int(time.time()*1000))

        default_par={
            'client_id':self.__client_id,
            'access_token':res['access_token'],
            'sign':self.calc_sign(self.__client_id+res['access_token'] + t + self.stringToSignPOST(json.dumps(body), '', url), self.__secret),
            't':t,
            'sign_method':'HMAC-SHA256'
            }
        r = requests.put(self.__base + url, headers=dict(default_par,**headers), data=json.dumps(body))
        r = json.dumps(r.json(), indent=2, ensure_ascii=False) # Beautify the request result format for easy printing and viewing
        return r

    def GetDeviceStatus(self):
        print("Get Status of" + self.__device_id)
        r = self.GET(url = '/v1.0/devices/' + self.__device_id + '/status')
        print(r)

    def GetDeviceFunction(self):
        print("Get Function List of" + self.__device_id)
        r = self.GET(url = '/v1.0/devices/' + self.__device_id + '/functions')
        print(r)

    def IR_TVControlOnOff(self, IR_ID, TV_ID):
        d = {"key": "Power"}
        r = self.POST(url = '/v1.0/infrareds/' + IR_ID + '/remotes/' + TV_ID +'/command', body=d)
        return(r)

    def IR_AirConditionControl(self, IR_ID, remote_id, power, mode, temp, wind, d):
        print("Control Air Conditioner Remote")
        r = self.POST(url = '/v1.0/infrareds/' + IR_ID + '/air-conditioners/' + remote_id +'/command', body=d)
        print(r)

    def device_control(self, cmd):
        d = {"commands":[cmd]}
        print(d)
        global returnCmd
        try:
            r = self.POST(url = f'/v1.0/devices/{self.__device_id}/commands', body=d)
            print(r)
            returnCmd = json.loads(r)
        except:
            print('Cannot control')
        if not (returnCmd.get('success') is None):
            if(returnCmd['success'] == False):
                if(returnCmd['msg'] == 'token invalid'):
                    self.GetAccessToken()
