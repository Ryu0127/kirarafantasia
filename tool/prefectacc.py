#完美账号获取
import get5star
import tool.mission as mission
import time
import account

def maindo():
    print("正在注册账号...")
    a = account.signup()
    b = a [2]
    c = a [3]
    sessionid = account.login(b,c)[1]
    print("已完成账号注册，接下来将刷取初始8黄")
    get5star.get5star(sessionid,goalnum=8,firstflag=True,buguse=True)
    print("已完成第一轮刷取，接下来将获取突破石，本过程将重复150次")
    time.sleep(1)
    for i in range(150):
        get5star.get5star(sessionid, goalnum=8, firstflag=True, buguse=True)
    print("已完成第二轮刷取，接下来将刷取任务，耗时可能较长")
    time.sleep(1)
    for i in range(20):#确保任务都完成
        mission.doallmission(sessionid)
    print("已完成任务刷取")
    cc = account.getcontinuecode(sessionid)
    print("本账号引继码：%s,密码:%s,sessionid:%s"%(cc[1],cc[2],sessionid))
    time.sleep(1)
    #TODO :金币刷取（已完成，暂不公开）,道具刷取,关卡刷取，角色等级刷取（挖了个大坑）
maindo()