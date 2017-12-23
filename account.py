import uuid
from misc import *
from config import *

#python生成的json服务器似乎不认

def signup():
    api1 = 'player/signup'
    uuidr = str(uuid.uuid1())#uuid也是登录凭证之一。。。
    payload = '{"uuid":"'+uuidr+'","platform":2,"name":"'+getrangestr(8)+'","stepCode":1}'
    req = Torequest(api1,payload)
    return [0,req['playerId'],req['accessToken'],uuidr]

def login(accessToken,uuidt):
    api2 = 'player/login'
    payload = '{"uuid":"'+uuidt+'","accessToken":"'+accessToken+'","platform":2,"appVersion":"'+version+'"}'
    rep = Torequest(api2,payload)
    try:
        return [0, rep['sessionId']]
    except:
        return [-1,rep]

def getcontinuecode(sessionID):
    api = 'player/move/get'
    password = getrangestr(6)
    payload = r'{"password":"'+password+r'"}'
    rep = Torequest(api,payload,sessionID)
    try:
        return [0, rep['moveCode'],password]
    except:
        return [-1,rep]

def getacetokenfromCC(mc,mp):
    api = 'player/move/set'
    uuidg = str(uuid.uuid1())
    payload = '{"moveCode":"%s","movePassword":"%s","uuid":"%s","platform":2}'%(mc,mp,uuidg)
    rep = Torequest(api,payload)
    return [0,rep['accessToken'],uuidg]

def getallgift(sessionid):
    api = 'player/present/get_all'
    rep = Torequest(api,sessionid = sessionid,method = 'GET')
    pidl = []
    for pid in rep['presents']:
        pidl.append(pid['managedPresentId'])
    if not pidl:
        return [1]
    pidl = str(pidl)[1:-1]
    api2 = 'player/present/get?managedPresentId='+pidl.replace(" ","")+'&stepCode=0'
    Torequest(api2,sessionid =sessionid,method='GET')
    return [0]
