# -*- coding: utf-8 -*-
# @Time : 2021/8/2 10:51
# @Author : admin
# @File : test_teacher_resoure.py
# @Software: PyCharm
import pytest
import requests
import os
from requests_toolbelt import MultipartEncoder
import json

# os.environ['cloudHost'] ='http://222.128.6.177:8666'
# cloudHost=os.environ['cloudHost']
def test_getCurrentTeacher(loginfixSession):
    ss =loginfixSession
    url =os.environ['cloudHost']+'/cloudApi/teacherOperate/getCurrentLearnCatalogByBookId?bookId=1394455207337000961'
    res = ss.get(url)
    print(res.text)

def test_findBySubjectCodeAndParentId():
    # ss =loginfixSession
    url =os.environ['cloudHost']+'/cloudApi/catalog/findBySubjectCodeAndParentId?subjectCode=3&parentId=-1&createId=185'
    res = requests.get(url)
    print(res.text)
def test_getStudyTaskByPage(loginfixSession):
    ss =loginfixSession
    url =os.environ['cloudHost']+'/cloudApi/studentTask/getStudyTaskByPage'
    jsonss={"taskType":"","classId":"","name":"","beginTime":"","endTime":"","pageSize":10,"pageNum":1}
    res = ss.post(url,json=jsonss)
    print(res.text)
# 教师云上传文件(问题待解决，上传后时间不对)
def test_doUpload(loginfixSession):
    ss = loginfixSession
    url=os.environ['cloudHost']+'/cloudApi/fileUpload/doUpload'
    m= MultipartEncoder(
                    fields=[('bussCode','bookCatalog'),
                            ('file',('zxz.png',open(r'C:\Users\admin\PycharmProjects\api_Project_Pytest\case\ziyuanguanli\0_pic.png','rb'),'image/png'))
                            ]
    )
    res =ss.post(url,data=m,headers={'Content-Type':m.content_type})
    var2 = res.json()["data"]["resourceId"]
    print(var2)
    return var2
# 添加到教师云列表
def test_addCatalogResource(loginfixSession,doUpload):
    ss = loginfixSession
    resouredId=doUpload
    url=os.environ['cloudHost']+'/cloudApi/teacherOperate/addCatalogResource'
    jsonss = [{"refResourceId":resouredId,"fileName":"0_pic.png","refCatalogId":"1394455522459254785","orderNum":8,"shareState":"0","beginTime":None}]
    res =ss.post(url,json=jsonss)
    print(res.text)

