#! /usr/bin/env python
# -*- coding: utf-8 -*-
# 作者：研发部-温赫男
# 创建时间：2017年5月9日下午4:11:34
# 文档位置：

'''
'''

import re

from django.core.exceptions import ObjectDoesNotExist
from django.db import models

from define import ERRMSG, ERRMSG_DB


class Userdata(models.Model):
    userid = models.IntegerField(primary_key=True)
    username = models.CharField(max_length=45, blank=True, null=True)
    userpass = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'userdata'

    @classmethod
    def CreateUser(cls, username, userpass):
        '''
        注册,保存到数据库
        :param username: 
        :param userpass: 
        :return: 
        '''
        user = cls(username=username, userpass=userpass)
        user.save()

    @classmethod
    def UserLogin(cls, username, userpass):
        '''
        登录查询
        :param username: 
        :param userpass: 
        :return: 
        '''
        try:
            user = cls.objects.get(username=username,userpass=userpass)
            return user.userid
        except ObjectDoesNotExist:
            return None

    @classmethod
    def IsExistUser(cls, username):
        '''
        判断用户名是否被注册
        :param username: 
        :return: 
        '''
        try:
            cls.objects.get(username=username)
            return True
        except ObjectDoesNotExist:
            return False


class CVaild(object):
    @staticmethod
    def CheckUserName(username):
        '''
        检验用户名
        :param username: 
        :return: 
        '''

        if not (4 < len(username) < 45):
            return ERRMSG.USERNAME_WRONGLEN
        elif re.search("[^\w\d]+", username):
            return ERRMSG.USERNAME_WRONGCHAR

    @staticmethod
    def CheckUserPass(userpass):
        '''
        检验用户密码
        :param userpass:
        :return: 
        '''
        if 8 < len(userpass) < 16:
            return ERRMSG.USERNAME_WRONGLEN
        elif re.search("[^\w\d]+", userpass):
            return ERRMSG.USERNAME_WRONGCHAR
