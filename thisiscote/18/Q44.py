# 처음엔 min(abs(x1-x2), abs(y1-y2), abs(z1-z2))로 계산했었는데
# 각 행성들의 x축에서의 거리, y축에서의 거리, z축에서의 거리중 가장 작은값이 cost값
# 각 간선들의 최솟값을 계산해서 edges에 넣고 다시 정렬
# 최소 신장 트리리
n = int(input())

tb = [i for i in range(n+1)]

xs = []
ys = []
zs = []
edges = []

for i in range(n):
    x, y, z = map(int, input().split())
    # planet.append((x, y, z))
    xs.append((x, i))
    ys.append((y, i))
    zs.append((z, i))
xs.sort()
ys.sort()
zs.sort()

# (cost, 행성의 번호, 다음 연결된 행성 번호)
for i in range(n-1):
    edges.append((xs[i+1][0] - xs[i][0], xs[i][1], xs[i+1][1]))
    edges.append((ys[i+1][0] - ys[i][0], ys[i][1], ys[i+1][1]))
    edges.append((zs[i+1][0] - zs[i][0], zs[i][1], zs[i+1][1]))

def find_p(tb, a):
    if tb[a] != a:
        tb[a] = find_p(tb, tb[a])
    return tb[a]

def union_p(tb, a, b):
    x = find_p(tb, a)
    y = find_p(tb, b)
    if x < y:
        tb[b] = x
    else:
        tb[a] = y
# 간선 cost 정렬
edges.sort()
print(edges)
result = 0
cnt = 0
for edge in edges:
    cost, a, b = edge
    if find_p(tb, a) != find_p(tb, b):
        union_p(tb, a, b)
        cnt += 1
        result += cost
    if cnt == n-1:
        break
print(result)