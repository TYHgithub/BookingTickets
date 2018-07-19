#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import uuid
from piaowu.models import YuhuataiPerson
from piaowu.models import YuhuataiTeam
import qrcode

def register_person(card_id, visit_date):
    #print "debug:"+visit_date
    person = YuhuataiPerson.objects.filter(card_id=card_id,visit_date=visit_date)
    if len(list(person)) != 0:
        return False
    person = YuhuataiPerson.objects.create(card_id=card_id, visit_date=visit_date, people_number=1, user_uuid=uuid.uuid1())
    '''
    users = YuhuataiUser.objects.filter(card_id=card_id)
    users = list(users)
    if len(users) == 1:
        print("we already have your information in our database")
        #for user in users:
         #   img = qrcode.make(user.user_uuid)
          #  img.save(os.getcwd()+'/piaowu/static/images/qr_'+card_id+'.png')
        return False
    else:
        user = YuhuataiUser.objects.create(card_id=card_id, visit_date=visit_date,people_number = 1, user_uuid = uuid.uuid1())
        #img = qrcode.make(user.user_uuid)
        #img.save(os.getcwd() + '/piaowu/static/images/qr_' + card_id + '.png')
        print("register successfully")
        return True
    '''
    return True
def register_team(card_id, visit_date, people_number):
    team = YuhuataiTeam.objects.create(card_id=card_id, visit_date=visit_date, people_number=people_number, user_uuid=uuid.uuid1())

    return True
if __name__ == "__main__":
    #YuhuataiUser.objects.create(card_id=“220802199201014321”, telephone_number=“15212345678”,user_uuid="",register_date="")
    print "ok"