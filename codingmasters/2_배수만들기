import sys 
# 300의 배수중 가장 큰 300의 배수 구하기
# 0도 300의 배수이고, 없는 경우 -1 출력
# 300의 배수는 끝의 두자리수가 00 이고,
# 모든 자리의 각 숫자들의 합이 3으로 나뉘어져야함.

a = int(sys.stdin.readline()) 
arr = list(map(int, sys.stdin.readline().split()))

count, sum = 0, 0
for i in range(a):  # 0의 개수 세기
    if arr[i] == 0 :
        count += 1

# 내림차순 정렬
arr.sort(reverse=True)

if count == a: # 0의 개수가 a개 이면 0
    print(0)
elif count < 2: # 0의 개수가 2개 미만이면 300의 배수가 없으므로 -1
    print(-1)
else: # 0이 2개 이상 일 경우
    for i in arr:
        sum += i
    if sum % 3 == 0: # 모든 자리수의 합이 3의 배수이면
        s = ''
        for i in arr:
            s += str(i)
        print(s)
    else:
        print(-1)
    
    