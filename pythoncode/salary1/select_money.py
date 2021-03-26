#!/usr/bin/env python 
# -*- coding:utf-8 -*-
"@time:2021/3/26 2:01 下午"
"@author:lydia_liu"
import money


def select_moeny():
    if money.saved_money == 2000:
        print(f"收到工资了！余额显示{money.saved_money}")
    else:
        print(f"还未收到工资！余额显示{money.saved_money}")
