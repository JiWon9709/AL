n = int(input())
k = list(map(int, input().split()))
d = [0] * 100
# a(i) = max(a(i-1), a(i-2)+k(i))
# 1) 현재 식량창고를 털면 i-2번째부터 털수있고
# 2) i-1번꺼를 털면 현재 식량창고를 털수 없다.
d[0] = k[0]
d[1] = max(k[0], k[1])
for i in range(2, n):
    d[i] = max(d[i-1], d[i-2] + k[i])
print(d[n-1])