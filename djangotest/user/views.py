#! /usr/bin/env python
# -*- coding: utf-8 -*-
# 作者：研发部-温赫男
# 创建时间：2017年5月9日下午4:07:01
# 文档位置：

'''
'''
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import Context, loader
from django.views.decorators.csrf import csrf_exempt

from define import ERRMSG_DB
import model


def login_view(request):
    errmsg = ""
    if request.method == "POST":
        username = request.POST.get("username")
        userpass = request.POST.get("password")
        errmsg = model.CVaild.CheckUserName(username)

        if errmsg == None:
            errmsg = model.CVaild.CheckUserPass(userpass)
        if errmsg == None:
            userid = model.Userdata.UserLogin(username,userpass)
            if userid:
                return HttpResponseRedirect("/loginok/?id=%s&name=%s"%(userid,username),)
            else:
                errmsg = ERRMSG_DB.USERINFO_NOTEXISTUSER


    return render_to_response('login.html', {"errmsg": errmsg})


def regok_view(request):
    return render_to_response('regok.html', {})

def loginok_view(request):
    username = request.GET.get("name")
    userid = request.GET.get("id")
    return render_to_response('loginok.html', {'username':username,'userid':userid})

def reg_view(request):
    errmsg = ""
    if request.method == "POST":
        username = request.POST.get("username")
        userpass = request.POST.get("password")
        errmsg = model.CVaild.CheckUserName(username)

        if errmsg == None:
            errmsg = model.CVaild.CheckUserPass(userpass)
        if errmsg == None:
            if model.Userdata.IsExistUser(username):
                errmsg =ERRMSG_DB.USERINFO_EXISTUSER
            else:
                errmsg = model.Userdata.CreateUser(username, userpass)
                if errmsg == None:
                    return HttpResponseRedirect("/regok/")

    return render_to_response('reg.html', {"errmsg": errmsg})
