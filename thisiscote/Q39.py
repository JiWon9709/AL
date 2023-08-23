# 화성 탐사
# 출발 > 목표 지점 이동 시 항상 최적의 경로를 찾아야함
# 입력이 n^2 이므로 10000을 넘길수 있음 플로이드 워셜 알고리즘 x => 다익스트라
# 각 칸을 노드로 보고 인접한 노드가 연결 되어있다고 생각하기
import sys
import heapq
INF = int(1e9)
t = int(sys.stdin.readline())
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

for _ in range(t):
    n = int(sys.stdin.readline())
    graph = []
    for i in range(n):
        graph.append(list(map(int, sys.stdin.readline().split())))

    distance = [[INF] * n for _ in range(n)]
    # print(distance)
    x, y = 0, 0
    q = [(graph[x][y], x, y)]
    distance[x][y] = graph[x][y]

    while q:
        dist, x, y = heapq.heappop(q)
        if distance[x][y] < dist:
            continue
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= n or ny < 0 or ny >= n:
                continue
            cost = dist + graph[nx][ny]
            if cost < distance[nx][ny]:
                distance[nx][ny] = cost
                heapq.heappush(q, (cost, nx, ny))
    print(distance[n-1][n-1])
# def short_path(n):
#     dp = [[0] * n for _ in range(n)]
#     for i in range(n):
#         arr = []
#         arr = list(map(int, sys.stdin.readline().split()))
#         # dp[i].append([a, b, c])
#         for j in range(n):
#             dp[i][j] = arr[j]
#     print(dp)
#     -1 1 0 0
#     0 0 1 -1
#     for k in range(n):
#         for a in range(n):
#             for b in range(n):
#                 if
#                     dp[a][b] = min(dp[a][b], dp[a][k] + dp[k][b])
#     print(dp[n-1][n-1])
#
# for _ in range(t):
#     n = int(sys.stdin.readline())
#     short_path(n)


