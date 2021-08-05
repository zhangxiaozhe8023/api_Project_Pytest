# -*- coding: utf-8 -*-
# @Time : 2021/8/4 17:47
# @Author : admin
# @File : conftest.py
# @Software: PyCharm
import pytest

@pytest.fixture(scope="session")
def login():
    print("用例先登录")