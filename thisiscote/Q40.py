# 노드로만 이루어져있을 경우 1차원 테이블을 만들고
# 초기화 그래프는 리스트를 n+1 개를 만들어 해당 노드에서 갈수있는 경로를 저장하는 방향으로 생각하기
import sys
import heapq
INF = int(1e9)
n, m = map(int, sys.stdin.readline().split())
# graph 초기화
graph = [[] for _ in range(n+1)]
# 방문시 최단경로
distance = [INF] * (n+1)
for _ in range(m):
    a, b = map(int, sys.stdin.readline().split())
    # graph[a-1][b-1] = 1
    # 양방향 a->b로 가는데 비용 1이라는 뜻
    graph[a].append((b, 1))
    graph[b].append((a, 1))
print(graph)
# 시작 노드 1번
start = 1
def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0
    while q:
        # 가장 최단 거리가 짧은 노드에 대한 정보 꺼내기
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        # 처리한 적이 없는 노드라면 인접한 노드들을 확인
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))
dijkstra(start)
max_node = 0
max_dist = 0
result = []
for i in range(1, n+1):
    if max_dist < distance[i]:
        max_node = i
        max_dist = distance[i]
        result = [max_node]
    elif max_dist == distance[i]:
        result.append(i)
print(max_node, max_dist, len(result))




