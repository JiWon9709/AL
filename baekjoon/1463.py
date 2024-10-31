from collections import deque
n = int(input())
q = deque()

dp = [0] * (n+1)
q.append(n)
cnt = 0

# dp
# for i in range(2, n+1):
#     dp[i] = dp[i-1] + 1
#     if i%2 == 0:
#         d[i] = min(d[i], d[i//2] +1)
#     if i % 3 == 0:
#         d[i] = min(d[i], d[i//3] + 1)
# print(d[n])

# bfs
while q:
    # print(q)
    x = q.popleft()
    if x == 1:
        break
    dp[cnt] = x
    if x % 3 == 0 and dp[x // 3] == 0:
        q.append(x//3)
        dp[x//3] = dp[x]+1
    if x % 2 == 0 and dp[x//2] == 0:
        q.append(x//2)
        dp[x//2] = dp[x]+1
    if dp[x-1] == 0:
        q.append(x-1)
        dp[x-1] = dp[x] + 1
    
print(dp[1])
    
