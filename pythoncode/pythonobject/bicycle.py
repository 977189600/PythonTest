#!/usr/bin/env python 
# -*- coding:utf-8 -*-
"@time:2021/3/20 3:28 下午"
"@author:lydia_liu"
"""
写一个 Bicycle (自行车)类，
    有 run （骑行）方法，调用时显示骑行里程km(骑行里程为传入的数字)
再写一个电动自行车类 EBicycle 继承 Bicycle，
    添加电池电量 battery_level 属性通过参数传入
    同时有两个方法：
    1、fill_charge(vol)  用来充电， vol为电量
    2、run(km) 方法用于骑行，每骑行10km消耗电量1度，
    当电量耗尽时调用Bicycle的run方法骑行，
    通过传入的骑行里程数，显示骑行结果（就是当电量耗尽，需要你真正骑的里程数）。
"""
#自行车
# class Bicycle:
#     def run(self,km):
#         print(f"骑行{km} km")
#
# #电自行车
# class EBicycle(Bicycle):
#     battery_level:int
#     def __init__(self,battery):
#         self.battery_level = battery
#     def fill_charge(self,vol):
#         self.battery_level += vol
#     def run(self,km):
#         miles = km - self.battery_level*10
#         if miles > 0:
#             print("电不够用")
#             print(f"使用电骑行：{self.battery_level*10}")
#             print(f"还需要骑行：{miles} km")
#             #Bicycle().run(miles)
#             super().run(miles)
#         else:
#             print("电够用")
#             print(f"骑行了{km} km")
# e1 = EBicycle(10)
# e1.run(101)

"""
写一个 Bicycle (自行车)类，
    有 run （骑行）方法，调用时显示骑行里程km(骑行里程为传入的数字)
再写一个电动自行车类 EBicycle 继承 Bicycle，
    添加电池电量 battery_level 属性通过参数传入
    同时有两个方法：
    1、fill_charge(vol)  用来充电， vol为电量
    2、run(km) 方法用于骑行，每骑行10km消耗电量1度，
    当电量耗尽时调用Bicycle的run方法骑行，
    通过传入的骑行里程数，显示骑行结果（就是当电量耗尽，需要你真正骑的里程数）。
"""
#自行车
class Bicycle():
    def run(self,km):
        print(f"可以骑行 {km} km")

#电动车
class EBicycle(Bicycle):
    battery_level:int
    def __init__(self,battery_level):
        self.battery_level = battery_level

    def fill_charge(self,vol): #充电的方法
        self.battery_level += vol

    def run(self,km):
       miles = km - self.battery_level*10
       if miles > 0:
            print(f"电不够用，使用电骑行了{self.battery_level*10} km")
            print(f"还需要脚蹬{miles} KM")
            #Bicycle().run(miles)
       else:
            print(f"电够用，骑行了{km} km")

e1 = EBicycle(10) #给10度电
e1.run(101)

