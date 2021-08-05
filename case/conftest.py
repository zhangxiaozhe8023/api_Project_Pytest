#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time : 2021/7/31 19:06
# @Author : apple
# @Software: PyCharm
import requests
import os
import pytest
from requests_toolbelt import MultipartEncoder
from case.common_login_function import CloudLoginClass
from case.login.func_login import login
from case.login import loginDemo

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
'''
登录的loginfixSession
'''
@pytest.fixture(scope='session')
def loginfixSession():
    s = requests.session()
    cloudloginclass = CloudLoginClass(s)
    ressession=cloudloginclass.loginFun()
    print ( '执行了cloud登录' )
    return ressession

# 命令行可设置不同的host参数
def pytest_addoption(parser):
    parser.addoption(
        "--cmdhost", action="store", default="http://222.128.6.177:8666", help="my option: type1 or type2"
    )
# autouse默认打开
@pytest.fixture(scope="session", autouse=True)
def host(request):
    '''获取命令行参数'''
    # 获取命令行参数给到环境变量
    os.environ['cloudHost'] = request.config.getoption("--cmdhost")
    print("当前用例运行测试环境22:%s"%os.environ["host"])

# 教师云上传文件[前置]
@pytest.fixture(scope="function")
def doUpload(loginfixSession):
    ss = loginfixSession
    url=os.environ['cloudHost']+'/cloudApi/fileUpload/doUpload'
    m= MultipartEncoder(
        fields=[('bussCode', 'bookCatalog'),
                ('file', (
                'zxz.png', open(r'C:\Users\admin\PycharmProjects\api_Project_Pytest\case\ziyuanguanli\0_pic.png', 'rb'),
                'image/png'))
                ]
    )
    res =ss.post(url,data=m,headers={'Content-Type':m.content_type})
    var2 = res.json()["data"]["resourceId"]
    print(var2)
    return var2