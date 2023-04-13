# -*- coding: UTF-8 -*-


import requests


def send_get(url, data):
    """ 定义send_get函数，
    用来接收参数，发送get请求 """
    r = requests.get(url=url, params=data)
    result = r.json()
    return result


def send_post(url, data):
    """ 定义send_post函数，
    用来接收参数，发送post请求 """
    r = requests.get(url=url, data=data)
    result = r.json()
    return result


def main(url, method, data):
    """ 定义一个主函数，根据method是get或post，来调用send_post()或send_get() """
    if method == 'POST':
        r = send_post(url, data)  # 如果是POST请求，则调用send_post()
    else:
        r = send_get(url, data)  # 如果是GET请求，则调用send_get()
    return r  # 将结果返回出去
