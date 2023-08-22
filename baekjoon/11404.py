# 문제를 제대로 읽지않아서 a->b 로 가는 경로가 여러가지인경우를 생각 하지않았었다.
import sys

n = int(sys.stdin.readline())
m = int(sys.stdin.readline())
INF = int(1e9)
dp = [[INF]*(n) for _ in range(n)]

for _ in range(m):
    a, b, c = map(int, sys.stdin.readline().split())
    if dp[a-1][b-1] > c: # a->b 로 가는 경우 더 작은 경로만 저장
        dp[a-1][b-1] = c

for k in range(n):
    for a in range(n):
        for b in range(n):
            dp[a][b] = min(dp[a][b], dp[a][k] + dp[k][b])

for i in range(n):
    for j in range(n):
        if i == j or dp[i][j] == INF: # 조건 추가:i에서 j로 갈 수 없는 경우에는 그 자리에 0을 출력한다.
            dp[i][j] = 0

for i in dp:
    print(*i)