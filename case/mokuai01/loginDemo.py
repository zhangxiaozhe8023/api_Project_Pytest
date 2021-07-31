# -*- coding:utf-8 -*-
# @Time : 2021/7/24 22:18
# @Author : apple
# @Software: PyCharm
import requests
import re
#学生云的登录的接口

def login(s):
    jsonParms={"account":"ceshi","password":"90db7a241ee36462c1d24a2cc45c1c8c"}
    url='http://222.128.6.177:8666/cloudApi/front/teacher/login'
    r=s.post(url,json=jsonParms)
    print('登录返回json是：%s'%r.text)
    print('登录cookie是：%s'%s.cookies)

def zuoCe():
    s= requests.session()
    url2='http://guanchu.tifenpai.com:9097/cloudApi/rolePower/getCurrentTeacherRoleAndPower'
    parms2={
        'teacherNowRoleId':'1248274854927663104'
    }
    r2=s.get(url2,params=parms2)
    print ( r2.text )
#
# url3='http://guanchu.tifenpai.com:9097/cloudApi/teacherOperate/getOldestCurrentCatalog'
# r3=s.get(url3)
# print('0000'+r3.text)
# 正则提取公式
# 知道前后取中间，遇到字符加转义
# name='csrfmiddlewaretoken' value='(.+?)'
# <span id="help"><a href="http://www.baidu.com/search/jubao.html" target
# url3='https://www.baidu.com/'
# r1=requests.post(url3,verify=False)
# print(r1.text)
# csrfmiddlewaretoken = re.findall('<span id="help"><a href="(.+?)" target', r1.text)
# print(csrfmiddlewaretoken[0])
if __name__ == '__main__':
    s =requests.session()
    login(s)
    # zuoCe()