import hashlib
import collections
import random
import requests
from config import *

def getrequesthash(api,sessionID = None,json1 = None):
    REQUESTHASH_SECRET = "85af4a94ce7a280f69844743212a8b867206ab28946e1e30e6c1a10196609a11"
    basestring = ''
    if sessionID != None:
        basestring = sessionID
    if basestring != None:
        basestring += " "
        basestring = basestring + "/api/" + api
    if json1 != None:
        basestring = basestring + " " + json1
    basestring = basestring + ' ' +REQUESTHASH_SECRET
    requesthash = hashlib.sha256(bytes(basestring,encoding="utf-8")).hexdigest()
    return requesthash

def getheader(apiurl,reqjson=None,X_STAR_SESSION_ID=None):
    if X_STAR_SESSION_ID != None:#登录与未登录
        header = collections.OrderedDict(
            [('Unity-User-Agent', 'app/0.0.0; Android OS 7.1.1 / API-25 NMF26F/7.11.16; Xiaomi MI MIX 2'),
             ('X-STAR-REQUESTHASH', getrequesthash(apiurl, sessionID=X_STAR_SESSION_ID, json1=reqjson)),
             ('X-Unity-Version', '5.5.4f1'),
             ('X-STAR-AB', X_STAR_AB),
             ('X-STAR-SESSION-ID', X_STAR_SESSION_ID),
             ('Content-Type', 'application/json; charset=UTF-8'),
             ('User-Agent', 'Dalvik/2.1.0 (Linux; U; Android 7.1.1; MI MAX 2 MIUI/7.11.16)'),
             ('Host', 'krr-prd.star-api.com'),
             ('Connection', 'Keep-Alive'),
             ('Accept-Encoding', 'gzip')])
    else:
        header = collections.OrderedDict(
            [('Unity-User-Agent', 'app/0.0.0; Android OS 7.1.1 / API-25 NMF26F/7.11.16; Xiaomi MI MIX 2'),
             ('X-STAR-REQUESTHASH', getrequesthash(apiurl,json1=reqjson)),
             ('X-Unity-Version', '5.5.4f1'),
             ('X-STAR-AB', X_STAR_AB),
             ('Content-Type', 'application/json; charset=UTF-8'),
             ('User-Agent', 'Dalvik/2.1.0 (Linux; U; Android 7.1.1; MI MAX 2 MIUI/7.11.16)'),
             ('Host', 'krr-prd.star-api.com'),
             ('Connection', 'Keep-Alive'),
             ('Accept-Encoding', 'gzip')])
    return header

def getrangestr(count):
    seed = "1234567890abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()_+=-"
    sa = []
    for i in range(count):
        sa.append(random.choice(seed))
    salt = ''.join(sa)
    return salt

def checkproxy():
    if proxycontrol == True:
        return {'http':http_proxy}
    else:
        return None

def Torequest(api,payload=None,sessionid=None):
    header = getheader(api,payload,sessionid)
    try:
        json1 = requests.post(api_host+api,data=payload,headers = header,verify = False,proxies = checkproxy()).json()
    except:
        raise ValueError("网络错误")
    if json1['resultCode'] != 0:
        try:
            error = errorlist[str(json1['resultCode'])]
        except:
            error = "未知错误："+ str(json1['resultCode'])
        raise ValueError(error)
    else:
        return json1