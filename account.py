import uuid
from misc import *
from str import *
import requests
import urllib3

urllib3.disable_warnings()  # 方便抓包

def checkproxy():
    if proxycontrol == True:
        return {'http':http_proxy}
    else:
        return None

#python生成的json服务器似乎不认

def signup():
    api1 = 'player/signup'
    uuidr = str(uuid.uuid1())#uuid也是登录凭证之一。。。
    payload = '{"uuid":"'+uuidr+'","platform":2,"name":"'+getrangestr(8)+'","stepCode":1}'
    header = getheader(apiurl=api1,reqjson=payload)
    req = requests.post(api_host+api1,data=payload,headers = header,verify = False,proxies = checkproxy()).json()
    return [0,req['playerId'],req['accessToken'],uuidr]

def login(accessToken,uuidt):
    api2 = 'player/login'
    payload = '{"uuid":"'+uuidt+'","accessToken":"'+accessToken+'","platform":2,"appVersion":"1.0.4"}'
    header = getheader(apiurl=api2,reqjson=payload)
    req = requests.post(api_host+api2,data=payload,headers = header,verify = False,proxies = checkproxy()).json()
    try:
        return [0, req['sessionId']]
    except:
        return [-1,req]

def getcontinuecode(sessionID):
    api = 'player/move/get'
    password = getrangestr(6)
    payload = r'{"password":"'+password+r'"}'
    header = getheader(apiurl=api,X_STAR_SESSION_ID=sessionID,reqjson=payload)
    rep = requests.post(api_host+api,data=payload,headers=header,verify = False,proxies = checkproxy()).json()
    try:
        return [0, rep['moveCode'],password]
    except:
        return [-1,rep]
