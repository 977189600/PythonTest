#!/usr/bin/env python 
# -*- coding:utf-8 -*-
"@time:2021/3/25 10:14 下午"
"@author:lydia_liu"

"""
课后作业：
1、补全计算器（加法，除法）的测试用例
2、使用数据驱动完成测试用例的自动生成
3、在调用测试方法之前打印【开始计算】，在调用测试方法之后打印【计算结束】
"""

from pythoncode.pytest.calculator import Calculator
import pytest
import yaml
import decimal


class TestCal:

    def setup(self):
        print("准备开始计算")

    def teardown(self):
        print("计算结束")

    y = yaml.safe_load(open("cal_data.yaml"))

    #测试相加功能
    @pytest.mark.parametrize("a,b,c",y["add"])
    def test_add(self,a,b,c):
        cal = Calculator()
        assert cal.add(a,b) == c

    #测试相减功能
    @pytest.mark.parametrize("a,b,c",y["plus"])
    def test_plus(self,a,b,c):
        cal = Calculator()
        assert cal.plus(a,b) == c

    # 测试相减功能
    @pytest.mark.parametrize("a,b,c", y["sub"])
    def test_sub(self,a,b,c):
        cal = Calculator()
        assert cal.sub(a, b) == c

    #测试相除的功能
    @pytest.mark.parametrize("a,b,c",y["div"])
    def test_divede(self,a,b,c):
        cal = Calculator()
        assert cal.divede(a,b) == c



