# 2583
import sys
from collections import deque
m, n, k = map(int, sys.stdin.readline().split())
graph = []
visited = [] # 왜 visited 2차 배열 쓰면 안될까....?
for _ in range(m):
    graph.append([0] * n)
    visited.append([0] * n)

for _ in range(k):
    x1, y1, x2, y2 = map(int, sys.stdin.readline().split())
    for i in range(y1, y2):
        for j in range(x1, x2):
            graph[i][j] = 1
# for i in range(m):
#     print(graph[i])
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
result = []
def bfs(x, y):
    queue = deque()
    queue.append((x,y))
    # visited[x][y] = 1
    size = 1
    graph[x][y] = 1
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < m and 0 <= ny < n:
                # if visited[nx][ny] == 0 and graph[nx][ny] == 0:
                #     visited[nx][ny] = 1
                if graph[nx][ny] == 0:
                    graph[nx][ny] = 1
                    queue.append((nx, ny))
                    size += 1
    result.append(size)

# cnt = 0
for i in range(m):
    for j in range(n):
        if graph[i][j] == 0:
            bfs(i, j)
            # cnt += 1 모든 칸의 개수
result.sort()
print(len(result))
for i in range(len(result)):
    print(result[i], end=' ')