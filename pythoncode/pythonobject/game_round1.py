#!/usr/bin/env python 
# -*- coding:utf-8 -*-
"@time:2021/3/22 7:39 下午"
import random

"@author:lydia_liu"
"""
一个回合制游戏，每个角色都有hp和power,hp代表血量，power代表攻击力，hp的初始值为1000
power的初始值为200
定义一个fight方法：
my_final_hp = my_hp - enemy_power
enemy_final_hp = enemy_hp - my_power
两个hp进行对比，血量剩余多的人获胜
"""
def fight():
    my_hp = 1000
    my_power = 200
    enemy_hp = 1000
    enemy_power  = 120

    my_hp = my_hp - enemy_power
    enemy_hp = enemy_hp - my_power
    print(my_hp)
    print(enemy_hp)
    #三目表达式
    #print("我赢了")  if my_hp > enemy_hp else print("我输了")
    if my_hp > enemy_hp:
        print("我赢了")

    else:
        print("我输了")


# fight()
if __name__ == '__main__':
    hp = [x for x in range(990,1100)]
    print(hp)
    enemy_hp = random.choice(hp)
    print(enemy_hp)
    enemy_power = random.randint(1,)
    print(enemy_power)

    fight(enemy_hp,enemy_power)