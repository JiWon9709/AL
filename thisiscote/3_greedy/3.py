n, m = map(int, input().split())
lst = []
result = 0
for _ in range(n):
    lst.append(list(map(int, input().split())))
    min_val = min(lst)
    result = max(result, min_val)
print(result)