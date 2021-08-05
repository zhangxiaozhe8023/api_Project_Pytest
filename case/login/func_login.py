import requests

def login(s):
    '''登录获取token'''
    # s = requests.session()  # 会话  代码里面的浏览器，模拟浏览器的功能
    url = "http://49.235.92.12:9000/api/v1/login"
    body = {
        "username": "test",
        "password": "123456"
    }

    # 转json
    r = s.post(url, json=body)
    print(r.json())

    # token
    token = r.json()["token"]
    print("取出token:%s" % token)

    h = {
        "Authorization": "Token %s" % token
    }
    s.headers.update(h)  # 更新到session会话
    # 更新之后的头部
    print(s.headers)
    return token

if __name__ == '__main__':
    s = requests.session()   # s单独拿出来
    token = login(s)   # 登录
    # 2.获取个人信息
    url2 = "http://49.235.92.12:9000/api/v1/userinfo"
    r2 = s.get(url2)
    print(r2.text)
#
# # 3.修改个人信息
# url3 = "http://49.235.92.12:9000/api/v1/userinfo"
# body = {
#     "name": "test",
#     "sex": "M",
#     "age": 20,
#     "mail": "283340479@qq.com"
#     }
# r3 = s.post(url3, json=body)
# print(r3.text)
