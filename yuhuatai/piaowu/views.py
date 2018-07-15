# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
import register.register_user as ru
import register.register as rg
import search.search as sc
import os


from django.views.decorators.csrf import csrf_exempt
import urllib
# Create your views here.
import urllib2
import json
from piaowu.models import YuhuataiPerson
from piaowu.models import YuhuataiBlacklist
import collections
#example:
# url = "https://api.weixin.qq.com/cgi-bin/usr/info?access_token=%s&openid=%s&lang=zh_CN"
# #分别填你的access_token,openid
# req = urllib2.Request(url%('access_token','openid'))
# #content是json类型的返回值 
# content = urllib2.urlopen(req).read()
# result = json.loads(content)
# msg = result.get('key')

@csrf_exempt
def wx(request):
    redirect_para = {
        #'appid':'wx4b80856c56b3ffd9',
        'appid':'wx1f3fafdacfa38a4c',
        'redirect_uri':'http://111.231.93.28/wx_in/',
        'response_type':'code',
        'scope':'snsapi_base',
        'state':123,
        'connect_redirect':1,
        }
    params = urllib.urlencode(redirect_para)
    redirect_url = "https://open.weixin.qq.com/connect/oauth2/authorize?%s#wechat_redirect" % params
    # web wang ye shou quan jie kou
    #https://open.weixin.qq.com/connect/oauth2/authorize?appid=wx520c15f417810387&redirect_uri=https%3A%2F%2Fchong.qq.com%2Fphp%2Findex.php%3Fd%3D%26c%3DwxAdapter%26m%3DmobileDeal%26showwxpaytitle%3D1%26vb2ctag%3D4_2030_5_1194_60&response_type=code&scope=snsapi_base&state=123#wechat_redirect'
    #return HttpResponseRedirect(redirect_url)
    print(redirect_url)
    return render(request,'redirect.html', {'redirect_url':redirect_url})

@csrf_exempt
def wx_in(request):
    if request.method =='GET':# wechat
        code = request.GET.get('code')
        state =  request.GET.get('state')
        #openid = get_openid(code)
        #token_interface = "https://api.weixin.qq.com/sns/oauth2/access_token?appid=wx1f3fafdacfa38a4c&secret=addb1018b7137807c41eb2e0f29bde77&code=%s&grant_type=authorization_code" % code
        #new = ru.new_user(openid)
        try:
            openid = request.session['openid']
            try:
                user = WxUser.objects.get(openid=openid)
                new = False
            except:
                new = True
            dicts = {'code':code, 'state':state, 'new':new}
        except:
            dicts = {'code':code, 'state':state, 'new':True}
        return render(request, 'register_wx.html', dicts)
    else:
        return render(request, 'register_wx.html', {})

@csrf_exempt
def register_wx(request):
    print(request.method)
    print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
    if request.method == "POST":
        card_id = request.POST.get('card_id')
        telephone_number = request.POST['telephone_number']
        code = request.POST['code']

        openid = get_openid(code)
        request.session['openid'] = openid
        print(openid)
        first_register = ru.register_user_wx(openid, card_id, telephone_number)

        qr_code = '/static/images/qr_' + openid + '.png'

        print("###################################")
        print(qr_code)
        return render(request, 'register_wx.html', {'qr_code': qr_code, "first_register": first_register, 'new':False})
    return render(request, 'register_wx.html', {})

@csrf_exempt
def search_wx(request): #for wechat
    try:
        openid = request.session['openid']
        user = WxUser.objects.get(openid=openid)
        card_id = user.card_id
        qr_code = '/static/images/qr_' + openid + '.png'
        return render(request, 'search_wx.html', {'qr_code':qr_code, 'notice':"hahaha"})
    except:
        return HttpResponse("no user")

@csrf_exempt
def index(request):
    return render(request,'register.html',{})


@csrf_exempt
def register(request):
    if request.method == 'POST':
        card_id = request.POST['card_id']
        telephone_number = request.POST['telephone_number']
        code = request.POST['code']
        openid = False
        first_register = ru.register_user(openid, card_id, telephone_number)

        qr_code = '/static/images/qr_' + card_id + '.png'
        return render(request, 'register.html', {'qr_code': qr_code, "first_register": first_register})
    return render(request, 'register.html', {})


@csrf_exempt
def get_openid(code):
    #token_interface = "https://api.weixin.qq.com/sns/oauth2/access_token?appid=wx4b80856c56b3ffd9&secret=3d83eb571b2da051761cf25f2fcc98c1&code=%s&grant_type=authorization_code" % code
    token_interface = "https://api.weixin.qq.com/sns/oauth2/access_token?appid=wx1f3fafdacfa38a4c&secret=addb1018b7137807c41eb2e0f29bde77&code=%s&grant_type=authorization_code" % code
    #info = method_get_api(token_interface)
    req = urllib2.Request(token_interface)
    res = urllib2.urlopen(req).read()
    info = json.loads(res)
    print(info)
    access_token = info.get('access_token')
    openid = info.get('openid')
    return openid

def index_register_person(request):
    return render(request,'register_person.html')
def index_register_team(request):
    return render(request,'register_team.html')
def index_search_person(request):
    return render(request,'search_person.html')
def index_search_team(request):
    return render(request,'search_team.html')
def register_person(request):
    name = request.POST['name']
    profession=request.POST['profession']
    card_id = request.POST['card_id']
    visit_date = request.POST['visit_date']
    if visit_date.startswith("<"):
        visit_date = request.POST['visit_date2']
    '''
    year = request.POST['YYYY']
    month = request.POST['MM']
    day = request.POST['DD']
    if len(month) == 1:
        month = "0"+month
    if len(day) == 1:
        day = "0"+day
    '''
    ret_msg=""
    blackperson = YuhuataiBlacklist.objects.filter(card_id=card_id)
    if len(list(blackperson)) != 0:
        ret_msg = "对不起，您的证件号已被加入黑名单，不能预约！"
    else:
        ret = rg.register_person(card_id, visit_date)
        if ret == True:
            ret_msg = "预约成功！您已预约"+visit_date+"参观雨花台，请于当日携本人身份证入场！"
        else:
            ret_msg = "对不起，您已预约过"+visit_date+"参观雨花台，每人每日仅能预约一次！"
    return render(request, 'register_person.html', {'ret_msg': ret_msg,'name':name,'profession':profession,'card_id':card_id,'visit_date':visit_date})
def register_team(request):
    card_id = request.POST['card_id']
    year = request.POST['YYYY']
    month = request.POST['MM']
    day = request.POST['DD']
    if len(month) == 1:
        month = "0" + month
    if len(day) == 1:
        day = "0" + day
    people_number = request.POST['people_number']
    ret = rg.register_team(card_id, year+"-"+month+"-"+day,people_number)
    ret_msg = "预约成功!"
    return render(request, 'register_team.html', {'ret_msg': ret_msg})
def search_person(request):
    card_id = request.POST['card_id']
    persons = sc.search_person(card_id)

    ret_res =  {}
    ret_persons = collections.OrderedDict()
    if len(persons) == 0:
        ret_res["您还没有预约!"]=""
    else:
        ret_res["身份证号"]="预约日期"
        for p in persons:
            ret_persons[p] = p.visit_date
    '''
    ret_msg = "您的二维码如下："
    qr_code = ""
    if ret == True:
        qr_code = '/static/images/persons/qr_' + card_id + '.png'
        return render(request, 'search_person.html', {'qr_code': qr_code, "ret_msg": ret_msg})
    ret_msg = "您还没有预约，请点击如下链接进行个人预约"
    register_link = "http://yuhuatai/register_person.html"
    '''
    return render(request, 'search_person.html', {'ret_res':ret_res, 'ret_persons': ret_persons,'card_id':card_id})

def search_team(request):
    card_id = request.POST['card_id']
    ret = sc.search_team(card_id)
    ret_msg = "您的二维码如下："
    if ret == True:
        qr_code = '/static/images/teams/qr_' + card_id + '.png'
        return render(request, 'search_team.html', {'qr_code': qr_code, "ret_msg": ret_msg})
    ret_msg = "您还没有预约，请点击如下链接进行团体预约"
    register_link = "http://yuhuatai/register_team.html"
    return render(request, 'search_team.html', {'register_link': register_link, "ret_msg": ret_msg})


    
