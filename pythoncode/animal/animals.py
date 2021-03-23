#!/usr/bin/env python 
# -*- coding:utf-8 -*-
"@time:2021/3/22 9:57 下午"
"@author:lydia_liu"

#比如创建一个类（Animal）【动物类】，类里有属性（名称，颜色，年龄，性别），类方法（会叫，会跑）
class Animal:
    name:str
    color:str
    age:int
    gender:str

    def __init__(self,name,color,age,gender):
        self.name = name
        self.color = color
        self.age = age
        self.gender = gender

    def call(self):
        print("会叫")

    def run(self):
        print("会跑")

#创建子类【猫】，继承【动物类】，
class Cat(Animal):
    cathair:str
    def __init__(self,name,color,age,gender,hair):
        # 复写父类的__init__方法，继承父类的属性
        super().__init__(name,color,age,gender)

        #添加一个新的属性，毛发 = 短毛，
        self.cathair = hair

        # 添加一个新的方法， 会捉老鼠，
    def catch(self):
        #print(f"{self.name}会抓老鼠")
        return f"{self.name}会抓老鼠"


        # 复写父类的‘【会叫】的方法，改成【喵喵叫】
    def call(self):
         print(f"{self.name} 喵喵叫")
        #return f"{self.name} 喵喵叫"

# 创建子类【狗】，继承【动物类】，
class Dog(Animal):
    doghair:str
# 复写父类的__init__方法，继承父类的属性，
    def __init__(self,name,color,age,gender,hair):
        super().__init__(name,color,age,gender)
#
# 添加一个新的属性，毛发=长毛，
        self.doghair = hair
# 添加一个新的方法， 会看家，
    def carehome(self):
        print(f"{self.name} 会看家！")

# 复写父类的【会叫】的方法，改成【汪汪叫】
    def call(self):
        print(f"{self.name} 汪汪叫")

