# 2979
import sys

cost = list(map(int, sys.stdin.readline().split()))
car = []
# 트럭이 주차 되있는 시간
for i in range(3):
    car.append([0] * (101))

for i in range(3):
    start, end = map(int, sys.stdin.readline().split())
    for j in range(start, end):
        car[i][j] = 1
sum = 0
for i in range(101):
    lv = 0
    for j in range(3):
        if car[j][i] == 1:
            lv += 1
    if lv > 0:
        lv -= 1
        sum += cost[lv] * (lv + 1)
    else:
        continue
print(sum)
