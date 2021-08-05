#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time : 2021/7/31 19:13
# @Author : apple
# @Software: PyCharm
import os

import requests
os.environ['host'] = 'http://222.128.6.177:8666'
cloudHost=os.environ.get('host')

class CloudLoginClass():
    def __init__(self,s):
        self.s=s
    def loginFun(self):

        jsonParms = {"account": "yingyu.", "password": "2501921fa8bbcda5480caf9cbecfdd3d"}
        url = cloudHost + '/cloudApi/front/teacher/login'
        r = self.s.post(url, json=jsonParms)
        print('登录返回json是：%s' % r.text)
        print('登录cookie是：%s' % self.s.cookies)
        return self.s