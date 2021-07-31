#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time : 2021/7/31 19:13
# @Author : apple
# @Software: PyCharm
def login(s):
    jsonParms={"account":"ceshi","password":"90db7a241ee36462c1d24a2cc45c1c8c"}
    url='http://222.128.6.177:8666/cloudApi/front/teacher/login'
    r=s.post(url,json=jsonParms)
    print('登录返回json是：%s'%r.text)
    print('登录cookie是：%s'%s.cookies)