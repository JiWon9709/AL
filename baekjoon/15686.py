import sys
from itertools import combinations
# 0: 빈칸, 1: 집, 2: 치킨집
# 구현 완전탐색, 백트래킹
# 1e9 : 최대값 설정, 10억 이내
n, m = map(int, sys.stdin.readline().split())
city = []
house, chick = [], []
for _ in range(n):
    city.append(list(map(int, sys.stdin.readline().split())))
for i in range(n):
    for j in range(n):
        if city[i][j] == 1:
            house.append((i, j))
        elif city[i][j] == 2:
            chick.append((i, j))
# 조합
comb = list(combinations(chick, m))
def get_sum(c):
    res = 0
    for x, y in house:
        temp = 1e9
        for cx, cy in c:
            temp = min(temp, abs(x- cx) + abs(y - cy))
        res += temp
    return res

result = 1e9
for c in comb:
    result = min(result, get_sum(c))
print(result)

# # 백트래킹
# arr = []
# check = int(1e9)
# def back(num, cnt):
#     global check
#     if num > len(chick):
#         return
#     if cnt == m:
#         result_tot = 0
#         for hx,hy in house:
#             min_check = int(1e9)
#             for idx in arr:
#                 cx,cy = chicken[idx]
#                 min_check = min(min_check,abs(hx-cx)+abs(hy-cy))
#
#             result_tot+=min_check
#
#         real_check = min(result_tot,check)
#         return
#     arr.append(num)
#     back(num+1, cnt+1)
#     arr.pop()
#     back(num+1, cnt)
#     return check
#
# (back(0, 0))