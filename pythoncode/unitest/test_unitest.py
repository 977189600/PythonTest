#!/usr/bin/env python 
# -*- coding:utf-8 -*-
"@time:2021/3/24 10:30 上午"
"@author:lydia_liu"
import unittest
class demo(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        print("setup class")
    @classmethod
    def tearDownClass(cls) -> None:
        print("teardown class")

    def setUp(self) -> None:
        print("setup")

    def tearDown(self) -> None:
        print("teardown")

    def test_case01(self):
        print("testcase01")
        self.assertEqual(2,2,"判断相等")
        self.assertIn('h','this')

    def test_case02(self):
        print("testcase02")
        self.assertEqual(1,1,"判断相等")
        self.assertIn('h','this')

    @unittest.skipIf(1+1==2,"跳过测试用例")
    def test_case03(self):
        print("testcase03")
        self.assertEqual(2,4,"判断相等")
        self.assertIn('h','this')

class demo1(unittest.TestCase):
    def test_demo01_case0(self):
        print("test_demo1 case0")

    def test_demo01_case1(self):
        print("test_demo1 case1")

class demo2(unittest.TestCase):
    def test_demo02_case0(self):
        print("test_demo2 case0")

    def test_demo02_case1(self):
        print("test_demo2 case1")

if __name__ == '__main__':

    #第一种执行方式
    #unittest.main()

    #第二种执行方式
    # suite = unittest.TestSuite()
    # suite.addTest(demo("test_case01"))
    # suite.addTest(demo1("test_demo01_case0"))
    # unittest.TextTestRunner().run(suite)

    #第三种执行方式：此用法可以同时测试多个类
    # suite1 = unittest.TestLoader().loadTestsFromTestCase(demo)
    # suite2 = unittest.TestLoader().loadTestsFromTestCase(demo1)
    # suite = unittest.TestSuite([suite1,suite2])
    # unittest.TextTestRunner().run(suite)

    #第四种执行方式：匹配某个目录下所有以test开头的py文件，执行这些文件下的所有测试用例
    test_dir = "./"
    #discover可以一次调用多个脚本
    #test_dir被测试脚本的路径
    #pattern脚本名称匹配规则
    discover = unittest.defaultTestLoader.discover(test_dir,pattern="test*.py")
    unittest.TextTestRunner().run(discover)


