# +1 , -1, *2
# 최소 횟수 bfs
from collections import deque
n, k = map(int, input().split())

visited = [False] * 100001
visited[k] = True
q = deque([(k , 0)])

while q:
    current, cnt = q.popleft()
    if current == n:
        print(cnt)
        break
    
    next_nums = [current +1, current-1, current*2]
    
    for next_n in next_nums:
        if 0 <= next_n <= 100000 and not visited[next_n]:
            visited[next_n] = True
            q.append((next_n, cnt+1))