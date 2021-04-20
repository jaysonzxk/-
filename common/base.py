"""
author： mask
filename: base.py
datetime： 2021/3/19 0:26 
ide： PyCharm
"""
from common.requestmethod import myRequestMethod
import random
import string
import json


def get_phone(randomlength):
    """
    随机手机号
    string.digits=0123456789
    :return:
    """
    str_list = [random.choice(string.digits) for i in range(randomlength)]
    orderNo = "".join(str_list)
    phone = '13' + orderNo
    return phone


def get_host(env):
    """
    获取请求host
    :return:
    """
    with open(r'D:\work\app_api_test\config\host.json') as f:
        f = json.loads(f.read())
    if env == 'test':
        return f['app_test']
    else:
        return f['online']


def get_response(url, method, **kwargs):
    if method == "get":
        resp = myRequestMethod().get(url, **kwargs)
    if method == "post":
        resp = myRequestMethod().post(url, **kwargs)
    if method == "delete":
        pass
    if method == "put":
        pass
    return resp