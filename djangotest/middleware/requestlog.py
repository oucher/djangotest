#! /usr/bin/env python
# -*- coding: utf-8 -*-
# 作者：研发部-温赫男
# 创建时间：2017年5月9日下午6:13:43
# 文档位置：

'''
'''
from django.utils.deprecation import MiddlewareMixin


import logging
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

handler = logging.FileHandler("log/request.log")
handler.setLevel(logging.INFO)
logger.addHandler(handler)


fmt = logging.Formatter('%(asctime)s %(message)s')
handler.setFormatter(fmt)

#logger.propagate = False

def GetIP(request):
    if request.META.has_key('HTTP_X_FORWARDED_FOR'):
        ip = request.META['HTTP_X_FORWARDED_FOR']
    else:
        ip = request.META['REMOTE_ADDR']
    return ip

class SimpleMiddleware(MiddlewareMixin):
    '''记录访问日志
    '''
    def process_request(self, request):
        ip = GetIP(request)
        fullpath = request.get_full_path()
        logger.info("用户ip(%s),访问的url(%s)"%(str(ip),str(fullpath)))
        return None


