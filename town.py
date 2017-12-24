from misc import *

def sell(sessionid,itemid,number):
    api = 'player/item/sale'
    payload = '{"itemId":"%s","amount":"%s"}'
    Torequest(api,payload%(itemid,number),sessionid)
    return [0]