n, m = map(int, input().split())
kind = []
for _ in range(n):
    i = int(input())
    kind.append(i)

d = [10001] * (m+1)
d[0] = 0
# i = 금액 i 를 만들수잇는 최소한의 화폐개수 , k = 화폐의 단위
# a(i-k) = min(a(i), a(i-k) + 1)
for i in range(n):
    for j in range(kind[i], m+1):
        if d[j - kind[i]] != 10001:
            d[j] = min(d[j], d[j - kind[i]] + 1)
if d[m] == 10001:
    print(-1)
else:
    print(d[m])