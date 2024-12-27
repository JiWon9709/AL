# 최단 거리
# 다익스트라 - 한곳 -> 모든곳
# 플로이드 워셜 - 모든곳
n = int(input())
m = int(input())
bus_line = [[100001]*n for _ in range(n)]
for _ in range(m):
    i, j, cost = map(int, input().split())
    if bus_line[i-1][j-1] > cost :
        bus_line[i-1][j-1] = cost
    
# print(bus_line)
# min(B[i][j], B[i][k]+B[k][j])
for k in range(n):
    for i in range(n):
        for j in range(n):
            bus_line[i][j] = min(bus_line[i][j], bus_line[i][k]+bus_line[k][j])
            
for i in range(n):
    for j in range(n):
        if i == j or bus_line[i][j] >= 200002:
            bus_line[i][j] = 0

for i in bus_line:
    print(*i)
