# 1. 이중 for문 => 시간초과
# 2. 투 포인터
n = int(input())
arr = list(map(int, input().split()))
x = int(input())
cnt = 0
arr.sort()
# for i in range(n-1):
#     if arr[i] >= x:
#         break
#     else:
#         for j in range(i+1, n):
#             if arr[i] + arr[j] == x:
#                 cnt += 1
left = 0
right = n-1
while left < right:
    sum = arr[left] + arr[right]
    if sum == x:
        cnt += 1
        left += 1
    elif sum > x:  # 합이 x보다 크다면 제일큰 arr[right] 보다 작은값을 더해야하므로 right-1
        right -= 1
    else:
        left += 1
print(cnt)