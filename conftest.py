#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time : 2021/7/31 19:00
# @Author : apple
# @Software: PyCharm

import os
import pytest


def pytest_addoption(parser):
    parser.addoption(
        "--cmdhost", action="store", default="http://49.235.92.12:8020", help="my option: type1 or type2"
    )
# autouse默认打开
@pytest.fixture(scope="session", autouse=True)
def host(request):
    '''获取命令行参数'''
    # 获取命令行参数给到环境变量
    os.environ["host"] = request.config.getoption("--cmdhost")
    print("当前用例运行测试环境:%s"%os.environ["host"])
