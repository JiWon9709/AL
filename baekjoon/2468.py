# 2468
import sys
from collections import deque

n = int(input())
graph = [[0] * n for i in range(n)]
max_graph = 1
for i in range(n):
    for j, value in enumerate(list(map(int, sys.stdin.readline().split(' ')))):
        graph[i][j] = value
        if max_graph < graph[i][j]:
            max_graph = graph[i][j]

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
def bfs(x, y, h):
    queue = deque()
    queue.append((x, y))
    water[x][y] = 1 # 1씩 더했던거 고침, 상관없엇음 어차피 방문하지않으면 0 이므로
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n:
                if graph[nx][ny] > h and water[nx][ny] == 0:
                    water[nx][ny] = 1
                    queue.append((nx, ny))

# 최대 안전 영역 개수는 1개
# 노트를 못봤음 = "아무 지역도 물에 잠기지 않을 수도 있다."
max_cnt = 1 # 0 -> 1로 고치니까 통과
for h in range(1, max_graph):
    water = [[0] * n for i in range(n)]
    cnt = 0
    for i in range(n):
        for j in range(n):
            if water[i][j] == 0 and graph[i][j] > h:
                bfs(i, j, h)
                cnt += 1
    if max_cnt < cnt:
        max_cnt = cnt
print(max_cnt)