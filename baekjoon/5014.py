from collections import deque
f, s, g, u, d = map(int, input().split())

floor = [0] * (f+1)
q = deque([s])
floor[s] = 1

# bfs
while q:
    # print(q)
    now = q.popleft()
    if now == g:
        break
    if now+u <= f and  floor[now+u] == 0:
        floor[now+u] = floor[now]+1
        q.append(now+u)
    if  now-d > 0 and floor[now-d] == 0: 
        floor[now-d] = floor[now]+1
        q.append(now-d)
# print(floor)
if floor[g] == 0:
    print('use the stairs')
else:
    print(floor[g]-1)
        