# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.


from piaowu.models import YuhuataiPerson
from piaowu.models import YuhuataiTeam

admin.site.register(YuhuataiPerson)
admin.site.register(YuhuataiTeam)
