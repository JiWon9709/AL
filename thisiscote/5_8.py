def dfs(graph, v, visited):
    visited[v] = True # graph 방문기록
    print(v, end=' ')
    for i in graph[v]: #모든 그래프를 돌면서 인접한 노드들 탐색
        if not visited[i]: # 방문하지 않았다면
            dfs(graph, i, visited) # dfs 깊이탐색

graph = [
    [],
    [2, 3, 8],
    [1, 7],
    [1, 4, 5],
    [3, 5],
    [3, 4],
    [7],
    [2, 6, 8],
    [1, 7]
]

visited = [False] * 9
dfs(graph, 1, visited)