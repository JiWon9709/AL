def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b
        
n, m = map(int, input().split())
dp = [0] *(n+1)

for i in range(1, n+1):
    dp[i] = 1

for i in range(n):
    data = list(map(int, input().split()))
    for j in range(n):
        if data[j] == 1:
            union_parent(dp, i+1, j+1)

plan = list(map(int, input().split()))

result = True
for i in range(m-1):
    if find_parent(dp, plan[i]) != find_parent(dp, plan[i+1]):
        result = False

if result:
    print("yes")
else:
    print("no")    