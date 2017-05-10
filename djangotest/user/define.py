#! /usr/bin/env python
# -*- coding: utf-8 -*-
# 作者：研发部-温赫男
# 创建时间：2017年5月9日下午4:25:02
# 文档位置：

'''
'''

import enum


class ErrMsgDefine(str):
    def __new__(cls, codeid, msg):
        msgobj = str.__new__(cls, msg)
        msgobj.m_CodeID = codeid
        msgobj.m_ErrMsg = msg
        return msgobj


class ERRMSG(ErrMsgDefine, enum.Enum):
    USERNAME_WRONGLEN = (1101, "错误用户名长度")
    USERNAME_WRONGCHAR = (1102, "用户名包含错误字符")

    USERPASS_WRONGLEN = (1201, "错误密码长度")
    USERPASS_WRONGCHAR = (1202, "密码包含错误字符")

    def __str__(self):
        return "%s_%s" % (self.m_ErrMsg, self.m_CodeID)


class ERRMSG_DB(ErrMsgDefine, enum.Enum):
    DB_ERROR = (200001, "数据库未知错误")
    USERINFO_EXISTUSER = (200101, "用户已经存在")
    USERINFO_NOTEXISTUSER = (200102, "用户不存在或密码错误")
    USERINFO_WRONGPASS = (200103, "用户不存在或密码错误")
