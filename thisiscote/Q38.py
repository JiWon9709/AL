# 최단경로 문 - 플로이드워셜
import sys

INF = int(1e9)
n, m = map(int, sys.stdin.readline().split())
dp = [[INF] * (n+1) for _ in range(n+1)]
for i in range(n+1):
    for j in range(n+1):
        if i == j:
            dp[i][j] = 0
for _ in range(m):
    a, b = map(int, sys.stdin.readline().split())
    dp[a][b] = 1

for k in range(1, n+1):
    for a in range(1,n+1):
        for b in range(1, n+1):
            dp[a][b] = min(dp[a][b], dp[a][k]+dp[k][b])

cnt = 0
for i in range(1, n+1):
    count = 0
    for j in range(1, n+1):
        if dp[i][j] != INF or dp[j][i] != INF:
            count += 1
    if count == n:
        cnt += 1
print(cnt)
print(*dp)

# input 입력 세트
# 6 6
# 1 5
# 3 4
# 4 2
# 4 6
# 5 2
# 5 4