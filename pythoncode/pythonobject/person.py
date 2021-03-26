#!/usr/bin/env python 
# -*- coding:utf-8 -*-
"@time:2021/3/20 2:23 下午"
"@author:lydia_liu"
"""
创建一个Person 类
属性：姓名，性别，年龄，存款
方法：吃，睡，跑，赚钱
"""
import yaml
class Person:

    #静态属性
    name = None
    gender = "男"
    age = 0

    __money = 1000

    def __init__(self,name,gender,age):
        print("-----")
        self.name = name
        self.gender = gender
        self.age = age


    #动态行为
    def eat(self):
        print("eating")
    def sleep(self):
        print("sleeping")
    def running(self):
        print(f"{self.name} is running")
    def have_money(self): #通过公有方法访问私有属性
        return Person.__money
    def get_money(self):
        return self.__money + 1000

class Funny(Person):
    skill:str
    #继承Person类的属性和方法
    #自有的属性搞笑方法
    def __init__(self,name,gender,age,skill):
        # self.name = name
        # self.gender = gender
        # self.age = age
        super().__init__(name,gender,age)#与上面三行一致
        self.skill = skill

    def fun(self):
        print(f"{self.name} is funny")
class Singer(Person):
    def get_money(self):
        return "10000"

#实例化一个人，类的实例化
# p1 = Person("张三" ,30,"男")
# print(p1.name)
# print(p1.age)
# print(p1.gender)
# print(p1.eat())
# print(p1.sleep())
# print(p1.running())
# print(p1.have_money())
# print(dir(p1))

# fun1 = Funny("沈腾","男","30","搞笑")
# print(fun1.name)
# print(fun1.running())
# print(fun1.fun())
# print(fun1.skill)

# singer1 = Singer("周杰伦","男","31")
# print(singer1.get_money())

with open("../data/data.yaml",'r') as f:     #是将yaml格式转化成python对象
    data = yaml.safe_load(f)
#     file_content = f.read()
#     a = yaml.load(file_content,yaml.FullLoader)
print(data)
print(data["date1"][0])

print(yaml.safe_dump({"name": "hogwarts", "age": "20"})) #是将python转化为yaml格式

















