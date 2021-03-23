#!/usr/bin/env python 
# -*- coding:utf-8 -*-
"@time:2021/3/23 9:49 上午"
from pythoncode.animal.animals import Cat, Dog

"@author:lydia_liu"
import yaml
# 调用 name== ‘main’：
if __name__ == '__main__':

    with open("data.yaml") as f:
        date = yaml.safe_load(f)
        # print(date)
        # print(date["cat"][0])
    # 创建一个猫猫实例
    cat = Cat(name=date["cat"][0],color=date["cat"][1],age=date["cat"][2],gender=date["cat"][3],hair=date["cat"][4])


    # 调用捉老鼠的方法
    cat.catch()

    # 打印【猫猫的姓名，颜色，年龄，性别，毛发，捉到了老鼠】。
    print(f"猫猫的姓名:{cat.name} ,颜色:{cat.color} ,年龄:{cat.age} ,性别:{cat.gender} ,毛发:{cat.cathair},{cat.catch()}")

    # 创建一个狗狗实例
    dog = Dog(name=date["dog"][0],color=date["dog"][1],age=date["dog"][2],gender=date["dog"][3],hair=date["dog"][4])

    # 调用【会看家】的方法
    dog.carehome()

    # 打印【狗狗的姓名，颜色，年龄，性别，毛发】。
    print(f"狗狗的名字：{dog.name}, 颜色：{dog.color}, 年龄：{dog.age}, 性别：{dog.gender}, 毛发：{dog.doghair}")

