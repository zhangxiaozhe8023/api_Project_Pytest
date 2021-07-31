# -*- coding: utf-8 -*-
# @Time : 2021/7/28 14:25
# @Author : admin
# @File : readymlzxz.py
# @Software: PyCharm
import os
import yaml
def readyml2(ymlFile):
    if not os.path.isfile(ymlFile):
        raise FileNotFoundError ('文件路径没有找到，请检查:%s' % ymlFile)
    f = open(ymlFile,'r',encoding='utf-8')
    cfg = f .read()
    d = yaml.load(cfg,Loader=yaml.FullLoader)
    print("读取的测试文件数据：%s" % d)
    return d
if __name__ == '__main__':
    # 获取当前脚本所在的文件夹路径
    codefilePath = os.path.dirname(os.path.realpath(__file__))
    #     获取yaml的路径
    ymalfile = os.path.join(codefilePath, "test_data.yml")
    print(ymalfile)
    ss=readyml2(ymalfile)
    print(ss)
    print(type(ss))