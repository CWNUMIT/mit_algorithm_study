import sys
import math

# game loop
while True:
    enemyDic = dict()
    
    enemy_1 = input()  # name of enemy 1
    dist_1 = int(input())  # distance to enemy 1
    enemyDic[enemy_1] = dist_1
    
    enemy_2 = input()  # name of enemy 2
    dist_2 = int(input())  # distance to enemy 2
    enemyDic[enemy_2] = dist_2

    res = sorted(enemyDic.items(), key = (lambda x : x[1]))
    print(res[0][0])