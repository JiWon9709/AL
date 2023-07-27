import sys
from collections import deque
# 가장 긴 시간이 걸리는 육지 두 곳에 나뉘어 묻혀있다.
m, n = map(int, sys.stdin.readline().split())
arr = []
for _ in range(m):
    arr.append([line for line in sys.stdin.readline().rstrip()])
# print(arr)
dx, dy = [0, 0, 1, -1], [1, -1, 0, 0]

def move_short(x, y):
    queue = deque()
    queue.append((x, y))
    visited[x][y] = 1
    max_cnt = -1
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < m and 0 <= ny < n and arr[nx][ny] == 'L' and visited[nx][ny] == 0:
                queue.append((nx, ny))
                visited[nx][ny] = visited[x][y] + 1
                max_cnt = max(max_cnt, visited[nx][ny])
    return max_cnt - 1

cnt = -1
for i in range(m):
    for j in range(n):
        if arr[i][j] == 'L':
            visited = [[0] * n for _ in range(m)]
            cnt = max(cnt, move_short(i, j))
print(cnt)