n, m = map(int, input().split())
INF = 100000
scores = [[INF]*(n+1) for _ in range(n+1)]
for i in range(n+1):
    for j in range(n+1):
        if i == j:
            scores[i][j] = 0
            
for _ in range(m):
    i, j = map(int, input().split())
    scores[i][j] = 1 # i < j
for k in range(n+1):
    for j in range(n+1):
        for i in range(n+1):
            scores[i][j] = min(scores[i][j], scores[i][k]+scores[k][j])
            
# 순위 정해진거 찾기
# 나빼고 다른사람들이 순위가 다 정해지면 result +1
# retry
print(cnt)
