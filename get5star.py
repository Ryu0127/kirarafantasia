# 抽卡
# import requests
import collections
import json
import urllib3
from str import *
from requesthash import *

urllib3.disable_warnings()  # 方便抓包

def get5star(X_STAR_SESSION_ID, goalnum, playerid=None, chaidlist=None,
             firstflag=1):  # id,目标数，期望角色（仅限五星,传入ID,见str.py,list形式），playerid,是否第一次
    api1 = 'player/gacha/draw'
    payload1 = '{"gachaId":1,"drawType":3,"stepCode":0,"reDraw":true}'
    payload2 = '{"gachaId":1,"drawType":3,"stepCode":4,"reDraw":false}'  # python生成的json服务器不认，原因未知
    urhttp = urllib3.ProxyManager(http_proxy)
    while True:
        star5num = 0
        if firstflag == 1:  # 第一次无限十连请求值有所不同，检测选择
            payloadc = payload1
        else:
            payloadc = payload2
            firstflag = 1
        header = collections.OrderedDict(
            [('Unity-User-Agent', 'app/0.0.0; Android OS 7.1.1 / API-25 NMF26F/7.11.16; Xiaomi MI MIX 2'),
             ('X-STAR-REQUESTHASH', getrequesthash(api1, sessionID=X_STAR_SESSION_ID, json1=payloadc)),
             ('X-Unity-Version', '5.5.4f1'),
             ('X-STAR-AB', X_STAR_AB),
             ('X-STAR-SESSION-ID', X_STAR_SESSION_ID),
             ('Content-Type', 'application/json; charset=UTF-8'),
             ('User-Agent', 'Dalvik/2.1.0 (Linux; U; Android 7.1.1; MI MAX 2 MIUI/7.11.16)'),
             ('Host', 'krr-prd.star-api.com'),
             ('Connection', 'Keep-Alive'),
             ('Accept-Encoding', 'gzip')])
        # req = requests.session()
        # a = req.post(url1,headers = header,data =payload1 ,verify=False).json() #速度有点慢
        try:
            a = urhttp.request('post', api_host + api1, headers=header, body=payloadc, retries=10)
            a = json.loads(a.data.decode('utf-8'))
        except:
            print("网络故障，或服务器炸了,请检查str.py代理配置")
            return ['failed', '']
        try:
            b = a['managedCharacters']
        except:
            print("无数据")
            return ['failed', '']
        chaid = []
        starum = 0
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
        if cnamestr == None:
            cnamestr = "无"
        print(playeridstr + "本轮数量：" + str(star5num) + '  角色：' + cnamestr)
        if  chaidlist != None:
            if set(chaid) >= set(chaidlist) and star5num >= goalnum:
                return ['success', a]
        elif star5num >= goalnum:
            return ['success', a]
