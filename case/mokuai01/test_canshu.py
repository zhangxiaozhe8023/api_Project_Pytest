#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time : 2021/7/27 21:50
# @Author : apple
# @Software: PyCharm
import pytest
import json
import os
# 获取当前文件的绝对路径
from common.readymlzxz import readyml2


# 获取当前脚本所在的文件夹路径
coulFile =os.path.dirname(os.path.realpath(__file__))
# 拼接yaml路径
yamlFile2=os.path.join(coulFile,'test_data.yml')
print('拼接后的字符串%s'%yamlFile2)
# 读取yaml文件内容updata_info
testdata = readyml2(yamlFile2)['updata_info']
# 读取yaml文件内容updata_teacher_info
testdata_pdata_teacher_info = readyml2(yamlFile2)['updata_teacher_info']

# ,{"flag":True,"code":200,"message":"success","data":None,"success":True}
# testdata = ['ceshi01',{"flag":True,"code":200,"message":"success","data":None,"success":True}],['',{"flag":True,"code":200,"message":"success","data":None,"success":True}]
@pytest.mark.parametrize("nameParms, expect",testdata)
def test_update(loginfix ,nameParms,expect):
    s=loginfix
    parmsjson={"id":"1398194668294111232","name":nameParms,"beginTime":0,"endTime":0,"classIdList":["375","376"],"catalogIdList":["1323159304148353025","1323159394686599169","1323159658491543553","1330783338545545216","1330783502022737920","1330783519202607104","1330783549544202240","1330783584172376064"],"knowledgePointIdList":[]}
    url='http://222.128.6.177:8666/cloudApi/studentTask/addOrUpdateStudyTask'
    r=s.post(url,json=parmsjson)
    print(r.text)
    assert expect['code'] == r.json()['code']

@pytest.mark.guanli
@pytest.mark.parametrize('import_in,accpct',testdata_pdata_teacher_info)
def test_UpdataTeacher_Task(loginfix,import_in,accpct):
    s =loginfix
    ## headers中添加上content-type这个参数，指定为json格式
    headers = {'Content-Type': 'application/json'}
    url = 'http://222.128.6.177:8666/cloudApi/teacher/updateByTeacher/648'
    jsonData={"name":import_in,"password":"123456","tel":"100020000000","lessonId":"2"}
    response =s.put(url,data=json.dumps(jsonData),headers=headers)
    print(response.text)
    assert response.json()['code'] == accpct['code']
def test_UpdataTeacher(loginfix):
    s =loginfix
    ## headers中添加上content-type这个参数，指定为json格式
    headers = {'Content-Type': 'application/json'}
    url = 'http://222.128.6.177:8666/cloudApi/teacher/updateByTeacher/648'
    jsonData={"name":'张三',"password":"123456","tel":"100020000000","lessonId":"2"}
    response =s.put(url,data=json.dumps(jsonData),headers=headers)
    print(response.text)
