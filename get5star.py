# 抽首次十连
# import requests
import json
import urllib3
from misc import *
from config import proxycontrol

urllib3.disable_warnings()  # 方便抓包

def get5star(X_STAR_SESSION_ID, goalnum, playerid=None, chaidlist=None,
             firstflag=False):  # id,目标数，期望角色（仅限五星,传入ID,见str.py,list形式），playerid,是否第一次
    #eg:chalist = [111,222]
    api1 = 'player/gacha/draw'
    payload1 = '{"gachaId":1,"drawType":3,"stepCode":0,"reDraw":true}'
    payload2 = '{"gachaId":1,"drawType":3,"stepCode":4,"reDraw":false}'
    # python生成的json服务器似乎不认，原因未知
    if proxycontrol == True:
        urhttp = urllib3.ProxyManager(http_proxy)
    else:
        urhttp = urllib3.PoolManager()
    while True:
        star5num = 0
        if firstflag == False:  # 第一次无限十连请求值有所不同，检测选择 Test for the first time
            payloadc = payload1
        else:
            payloadc = payload2
            firstflag = True
        header = getheader(apiurl=api1,X_STAR_SESSION_ID=X_STAR_SESSION_ID,reqjson=payloadc)
        # req = requests.session()
        # a = req.post(url1,headers = header,data =payload1 ,verify=False).json() #速度有点慢 speed is slow
        try:
            a = urhttp.request('post', api_host + api1, headers=header, body=payloadc, retries=10)
            a = json.loads(a.data.decode('utf-8'))
        except:
            print("网络故障，或服务器炸了,请检查config.py代理配置")
            return [-1]
        try:
            b = a['managedCharacters']
        except:
            print("无数据")
            return [-1, a]
        chaid = []
        for c in b:
            if c['levelLimit'] == 50:
                star5num += 1
                chaid.append(c['characterId'])
        if playerid is not None:
            playeridstr = "playerid:" + str(playerid) + "       "
        else:
            playeridstr = ''
        cnamestr = ''
        for cname in chaid:
            cnamestr = cnamestr +'  '+chaname[str(cname)]
        if cnamestr == '':
            cnamestr = "无"
        print(playeridstr + "本轮数量：" + str(star5num) + '  角色：' + cnamestr)
        if  chaidlist != None:
            if set(chaid) >= set(chaidlist) and star5num >= goalnum:
                return [0, a]
        elif star5num >= goalnum:
            return [0, a]
