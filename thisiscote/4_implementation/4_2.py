n = int(input())
cnt = 0
for k in range(n+1):
    for j in range(60):
        for i in range(60):
            if '3' in str(i) + str(j) + str(k):
                cnt += 1

print(cnt)