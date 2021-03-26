#!/usr/bin/env python 
# -*- coding:utf-8 -*-
"@time:2021/3/25 10:18 下午"
"@author:lydia_liu"
import decimal
#实现计算器的相加功能
class Calculator:

    #相加
    def add(self,a, b):
        return a + b
    #相减
    def sub(self,a,b):
        return a - b
    #相乘
    def plus(self,a,b):
        return a * b
    #相除
    def divede(self,a,b):
        if b == 0:
            return "除数不能为0"
        else:
            return a / b