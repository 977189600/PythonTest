#!/usr/bin/env python 
# -*- coding:utf-8 -*-
"@time:2021/3/18 9:25 上午"
"@author:lydia_liu"
#a = 1
# def demo():
#     global a #告诉解释器，现在要使用外面的全局变量a
#     a = 2
#     print(a)
#     print(id(a))
# print(id(a))
# demo()
# print(id(a))

# def outer():
#     def ok():
#         print("inner")
#     return ok
# outer()()

'''
实现发礼物之后，展示礼物
1、默认值（have_gift）=false ，默认没有礼物
2、定义一个发礼物的方法
3、定义一个显摆礼物的方法
4、实现发礼物之后，能展示礼物
'''
have_gift = False

def send_gift():
    global  have_gift
    have_gift = True
    print("发礼物啦")
def show_gift():
    if have_gift == True:
        print("好开心，展示礼物啦！")
    else:
        print("礼物还未收到，等待礼物中！")
send_gift()
show_gift()

if __name__ == '__main__':
    send_gift()
    show_gift()