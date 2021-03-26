#!/usr/bin/env python 
# -*- coding:utf-8 -*-
"@time:2021/3/24 8:11 下午"
"@author:lydia_liu"
import allure

TEST_CASE_LINK = 'https://www.baidu.com'

@allure.testcase(TEST_CASE_LINK,"测试连接")
def test_with_testcase_link():
    pass
