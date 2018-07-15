# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
import django.utils.timezone as timezone

# Create your models here.

class WxUser(models.Model):
    openid = models.CharField(max_length=100)
    name = models.CharField(max_length=10, blank=True)
    card_id = models.CharField(max_length=18, blank=True)
    telephone_number = models.CharField(max_length=11, blank=True)
    user_uuid = models.CharField(max_length=36)
    subscribe_date = models.DateTimeField('预约日期',default = timezone.now)
    register_datetime = models.DateTimeField('保存日期',default = timezone.now)
    status = models.PositiveIntegerField('票务状态',default = 0) # 0:未使用;1:已使用;2:已过期;

    def __unicode__(self):
        # 在Python3中使用 def __str__(self):
        return self.openid

class YuhuataiPerson(models.Model):
    card_id = models.CharField(max_length=18,db_index=True)
    visit_date = models.DateField(default = None)
    people_number = models.IntegerField(default = None)
    user_uuid = models.CharField(max_length=36,primary_key=True)

    #register_datetime = models.DateTimeField('保存日期',default = timezone.now)

    def __unicode__(self):
        # 在Python3中使用 def __str__(self):
        return self.card_id

class YuhuataiTeam(models.Model):
    card_id = models.CharField(max_length=18,db_index=True)
    visit_date = models.DateField(default = None)
    people_number = models.IntegerField(default = None)
    user_uuid = models.CharField(max_length=36,primary_key=True)

    #register_datetime = models.DateTimeField('保存日期',default = timezone.now)

    def __unicode__(self):
        # 在Python3中使用 def __str__(self):
        return self.card_id
class YuhuataiBlacklist(models.Model):
    card_id = models.CharField(max_length=18, db_index=True, primary_key=True)

if __name__ == "__main__":
    #YuhuataiUser.objects.create(card_id=“220802199201014321”, telephone_number=“15212345678”,user_uuid="",register_date="")
    print "ok"
