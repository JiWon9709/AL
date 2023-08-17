import heapq
import sys

# input = sys.stdin.readline()
INF = int(1e9)

n, m, start = map(int, sys.stdin.readline().split())
graph = [[] for i in range(n+1)]
distance = [INF] * (n+1)
# print(n, m, start)
for _ in range(m):
    x, y, z = map(int, sys.stdin.readline().split())
    graph[x].append((y, z))
    # print(1)

def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0
    while q:
        dist, now = heapq.heappop(q)
        print(dist, now)
        if distance[now] < dist:
            continue
        for i in graph[now]:
            cost = dist + i[1]
            print(i, cost)
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

dijkstra(start)
count = 0
max_dist = 0
for d in distance:
    if d != INF:
        count += 1
        max_dist = max(max_dist, d)
print(count - 1, max_dist)