#完美账号获取（半自动）
import get5star
import tool.mission as mission
import time
import account
import tool.battle as battle
import town

global sessionid

def do1():#初始刷取
    print("请确保拥有一个良好的网络环境,config.py配置正确")
    print("整个过程大概耗时:45分钟，根据网络情况而定")
    time.sleep(1)
    print("正在注册账号...")
    a = account.signup()
    b = a [2]
    c = a [3]
    sessionid = account.login(b,c)[1]
    print("已完成账号注册")
    get5star.get5star(sessionid,goalnum=8,firstflag=True,buguse=True)
    print("已完成第一轮刷取，本账号sessionid:%s,本步骤恢复码:2")%sessionid
    time.sleep(1)

def do2(sessionid):#突破石刷取
    for i in range(150):
        get5star.get5star(sessionid, goalnum=8, firstflag=True, buguse=True)
        print("已完成第二轮刷取，,本账号sessionid:%s,本步骤恢复码:3")%sessionid
        time.sleep(1)

def do3(sessionid):#任务刷取
    for i in range(20):#确保任务都完成
        mission.doallmission(sessionid)
    print("已完成任务刷取")

def do4(sessionid):#金币刷取
    for i in range(150):
        battle.battleget(sessionid, "2015", "10000")
        town.sell(sessionid, "2015", "10000")
    print("已完成金币刷取")

def finalgetcc(sessionid):#获取引继码
    cc = account.getcontinuecode(sessionid)
    print("本账号引继码：%s,密码:%s,sessionid:%s"%(cc[1],cc[2],sessionid))
    time.sleep(1)

def maindo(rec=0,sessionidc =None):
    if rec == 0:
        do1()
        do2()
        finalgetcc()
    elif rec == 2:
        do2(sessionidc)
        finalgetcc(sessionidc)
    elif rec ==3:
        finalgetcc(sessionidc)

    #TODO :金币刷取（已完成，暂不公开）,道具刷取,关卡刷取，角色等级刷取（挖了个大坑）

maindo()