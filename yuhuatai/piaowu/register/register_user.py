#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import uuid
from piaowu.models import WxUser
import qrcode

def register_user_wx(openid, card_id, telephone_number):
    if openid: #wechat
        try:
            user = WxUser.objects.get(openid = openid)
            return False
        except:
            user = WxUser(openid = openid, card_id=card_id, telephone_number=telephone_number, user_uuid = uuid.uuid1())
            img = qrcode.make(user.user_uuid)
            img.save(os.getcwd() + '/piaowu/static/images/qr_' + openid + '.png')
            user.save()
            print("register successfully")
            return True

def new_user(openid): # to wechat
    try:
        user = WxUser.objects.get(openid = openid)
        return False
    except:
        return True

if __name__ == "__main__":
    #YuhuataiUser.objects.create(card_id=“220802199201014321”, telephone_number=“15212345678”,user_uuid="",register_date="")
    print "ok"