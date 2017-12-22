from get5star import *

def card():
    session = input("sessionid:")
    num = int(input("目标数量:"))
    FIRST = input("第一次抽卡（Y/N):")
    if FIRST == "Y":
        FIRST1 = True
    else:
        FIRST1 =False
    chaidli = input("目标角色（可选,填入id,以,间隔）:").split(",")
    ctr = ''
    chaidin = []
    if not chaidli:
        for ii in chaidli:
            chaidin.append(int(ii))
    else:
        chaidin = None
    while  ctr!= 0:
        success1 = get5star(session,goalnum=num,firstflag=FIRST1,chaidlist=chaidin)
        ctr = success1[0]

if __name__ == "__main__":
    try:
        card()
    except:
        print("输入有误")