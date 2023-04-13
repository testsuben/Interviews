# -*- coding: UTF-8 -*-

from test.base.test import main
import queue,time
from concurrent.futures import ThreadPoolExecutor,as_completed
"""
第一题
获取后写入txt文档：
"""

def get_mail(url):
    """
    请求获取邮箱地址

    :return:
    """

    print('--------开始抓取----------')
    data=main(url,"GET",None)
    email_list=[]
    for i in data:
        email=i["email"]
        email_list.append(email)
    return email_list

    # with open(r'C:\Users\Administrator\PycharmProjects\daletou\test\test.txt', "a") as file:  # 只需要将之前的”w"改为“a"即可，代表追加内容
    #     for j in email_list:
    #         file.write(j + "\n")

def run_get():

    with ThreadPoolExecutor(max_workers=10) as t:
        with open(r'test.txt',"a") as file:  # 只需要将之前的”w"改为“a"即可，代表追加内容
            obj_list = []
            begin = time.time()
            for page in range(1, 101):
                url = "https://jsonplaceholder.typicode.com/posts/{}/comments".format(page)
                obj = t.submit(get_mail,url)
                obj_list.append(obj)

            for future in as_completed(obj_list):
                data = future.result()
                for i in data:
                    file.write(i + "\n")
            times = time.time() - begin
            file.close()
            print(times)


if __name__ == '__main__':
    run_get()



