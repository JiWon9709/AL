# root 찾는함수
def find_parent(parent, a):
    if parent[a] != a:
        parent[a] = find_parent(parent, parent[a])
    return parent[a]
# 합연산
def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b
        
# 집 개수, 도로 개수
n, m = map(int, input().split())

# 초기 테이블, 자기자신의 root는 자기 자신
parent = [0]*(m+1)
for i in range(m+1):
    parent[i] = i
# 간선 정보, 최솟값
edges = []
result = 0
total = 0 # 전체 비용
# 도로 연결 노드, 비용값 입력
for _ in range(m):
    x, y, z = map(int, input().split())
    edges.append((z, x, y)) # 비용순으로 정렬하기 위해서 순서를 바꿔서 append
    total += z
# 간선을 비용순으로로 정렬
edges.sort()
# 간선 하나씩 확인
for edge in edges:
    cost, a, b = edge
    x = find_parent(parent, a)
    y = find_parent(parent, b)
    print(edge, x, y)
    # 사이클이 발생하지 않는 경우에만 집합에 포함
    if x != y:
        union_parent(parent, a, b)
        print(a, b, parent)
        result += cost

print(total - result)