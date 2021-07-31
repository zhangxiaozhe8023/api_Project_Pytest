#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time : 2021/7/31 19:06
# @Author : apple
# @Software: PyCharm
import pytest
import requests
from case.mokuai01.func_login import login
from case.mokuai01 import loginDemo

@pytest.fixture(scope="module")
def login_fix():
    '''自定义一个前置的操作'''
    print("先登陆")
    s = requests.session()
    login(s)
    return s

@pytest.fixture(scope="function")
def unlogin_fix():
    '''自定义一个前置的操作'''
    print("不登陆")
    s = requests.session()
    s.headers.update({"Authorization": "Token f4b9a1dffbf525ecc93f8c80035c60fa546d5xxx"})
    return s

@pytest.fixture(scope="function")
def add_testdata():
    print("新增测试数据")

# 练习pytest的fixture,级别不同，只需要修改scope的
# `"function"``
#    `"function"``     (default), ``"class"``, ``"module"``, ``"package"`` or ``"session"``.
@pytest.fixture(scope='session')
def loginfix():
    s = requests.session()
    loginDemo.login(s)
    print ( '执行了登录' )
    return s