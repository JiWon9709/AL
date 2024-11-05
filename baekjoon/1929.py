m, n = map(int, input().split())
arr = [] # 소수를 담을 리스트

if m <= 1:
    m += 1
for i in range(m, n+1):
    for j in range(2, int(i**0.5)+1): # 에라토스테네스의 체
        # 제곱근을 구해 제곱근의 약수를 구하면 약수를 포함하는 수를 모두 제거 가능
    # 아래코드로하면 시간초과
    # for j in range(2, i): # 2~i-1까지 소수는 나 자신과 1만 나누어짐
        if i % j == 0: #나누어지면 소수가 아님
            break
    else:
        arr.append(i)
for a in arr:
    print(a)