#!/usr/bin/env python 
# -*- coding:utf-8 -*-
"@time:2021/3/18 10:27 上午"
import money
"@author:lydia_liu"
def select_money():
    saved_money = money.saved_money
    if saved_money == 2000:
        print("收到工资了,工资余额显示2000！")
    else:
        print("还未收到工资,工资余额显示1000！")