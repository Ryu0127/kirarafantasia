from account import *

#仅供测试 不保证有效性 only for testing
#迟早会被封,所以没搞啥伪装(并不是因为懒
#！！！已失效！！！ --2017.12.24

def doallmission(sessionid):#一键完成当前所有任务(重复执行即可完成所有任务))
    api1 = 'player/mission/get_all'
    rep1 = Torequest(api1,sessionid = sessionid,method="GET")
    notdomission = []
    for mission in rep1['missionLogs']:
        if mission['state'] != 99:
            notdomission.append([mission['managedMissionId'],mission['missionId'],mission['subCode'],
                                 mission['rate'],mission['rateMax'],mission['limitTime']])
    if not notdomission:
        return [1,"all mission has done"]
    jsonstr = '{"missionLogs":[{"managedMissionId":%s,"missionID":%s,"subCode":%s,"rate":99,' \
              '"rateMax":%s,"state":1,"reward":null,"limitTime":"%s"}]}'
    errmsid = []
    cgc = 0
    for req in notdomission:
        api2 = 'player/mission/set'
        Torequest(api2,payload= jsonstr % (req[0],req[1],req[2],req[4],req[5]),sessionid =sessionid)
        try:
            api3 = 'player/mission/complete'
            jsonstr2 = '{"managedMissionId":%s}'% req[0]
            Torequest(api3 ,jsonstr2,sessionid)
            cgc += 1
            if cgc ==90:#防到99自动清除
                getallgift(sessionid)
                cgc = 0
        except ValueError:
            errmsid.append(req[0])
    getallgift(sessionid)
    if not errmsid:
        return [0]
    else:
        return [2,errmsid]