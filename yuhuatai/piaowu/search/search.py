#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import uuid
from piaowu.models import YuhuataiPerson
from piaowu.models import YuhuataiTeam
import qrcode

def search_person(card_id):
    person = YuhuataiPerson.objects.filter(card_id=card_id)
    person = list(person)
    return person
def search_team(card_id):
    team = YuhuataiTeam.objects.filter(card_id=card_id)
    team = list(team)
    if len(team) >= 1:
        for t in team:
            img = qrcode.make(t.user_uuid)
            img.save(os.getcwd() + '/piaowu/static/images/teams/qr_' + card_id + '.png')
            return True
    else:
        print("The team has not registered")
        return False
    return True
if __name__ == "__main__":
    #YuhuataiUser.objects.create(card_id=“220802199201014321”, telephone_number=“15212345678”,user_uuid="",register_date="")
    print "ok"