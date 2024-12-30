n, m, k = map(int, input().split())
lst = list(map(int, input().split()))
lst.sort()
# print(lst)
result = 0
cnt = 0
for _ in range(m):
    if cnt == m:
        break
    # big = lst[n-1]
    if lst[n-2] != lst[n-1]:
        result += lst[n-2]
        cnt += 1
    for j in range(k):
        result += lst[n-1]
        cnt += 1
# 가장 큰수가 더해지는 횟수
# count = (m / (k+1))*k + m % (k+1)
print(result)