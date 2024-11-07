x = int(input())

# n=2: 1/1
# n=3: 1/2, 2/1
# n=4: 3/1, 2/2, 1/3
# n=5: 1/4, 2/3, 3/2, 4/1
# n=6: 5/1, ,,,
# 규칙: 합이 2부터 시작, 합과 개수가 +1씩 증가, 1 시작이 짝수일때
# n * (n-1) / 2 = 합
n = 2
while n:
    sum = n*(n-1) // 2
    if sum >= x:
        if n % 2 == 0: # 짝수인경우, (?,1)시작 /홀수일 경우 (1,?) 시작
            print(f"{n - (x - (n-1)*(n-2)//2)}/{x - (n-1)*(n-2)//2}")
        else:
            print(f"{x - (n-1)*(n-2)//2}/{n - (x - (n-1)*(n-2)//2)}")
        break
    n += 1