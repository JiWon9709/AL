# 1012
# 배추가 이어져있는 영역 개수 구하기
# 테스트케이스 수 만큼 실행
import sys
from collections import deque
t = int(sys.stdin.readline().rstrip())

def find_cabbage(x, y):
    queue = deque()
    queue.append((x, y))
    graph[x][y] = 0
    dx = [0, 1, -1, 0]
    dy = [1, 0, 0, -1]
    while queue:
        a, b = queue.popleft()
        for i in range(4):
            nx = a + dx[i]
            ny = b + dy[i]
            if 0 <= nx < n and 0 <= ny < m and graph[nx][ny] == 1:
                queue.append((nx, ny))
                graph[nx][ny] = 0

for i in range(t):
    m, n, k = map(int, sys.stdin.readline().split())
    graph = []
    count = 0
    for j in range(n):
        graph.append([0] * m)
    for l in range(k):
        y, x = map(int, sys.stdin.readline().split())
        # print(x, y)
        graph[x][y] = 1
    for a in range(n):
        for b in range(m):
            if graph[a][b] == 1:
                find_cabbage(a, b)
                count += 1
    print(count)
