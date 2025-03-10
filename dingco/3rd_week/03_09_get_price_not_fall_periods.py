from collections import deque
prices = [1, 2, 3, 2, 3]

# [1, 2, 3, 2, 3]
# 1 2 3 2 3
# 2 3 2 3
# 3 2 3
def get_price_not_fall_periods(prices):
    res = [0] * len(prices)
    n = len(prices) # 5
    # 가격이 떨어지지 않은 기간 구하기
    queue = deque(prices)
    while queue: # 큐에 price가 있는동안
        price = queue.popleft() # 한개씩 fifo로 빼면서
        period = 0
        for idx in range(len(queue)): # 오른쪽으로 하나씩 비교
            if price > queue[idx]: # 만약 주식가격이 떨어졌다면
                res[n - len(queue)-1] = period +1 # 바로 옆에서 떨어진것이므로 +1
                break
            else: # 같거나 높으면 기간 +1
                period += 1
        else:
            res[n - len(queue)-1] = period
        # print(queue, period)

    return res


print(get_price_not_fall_periods(prices))

print("정답 = [4, 3, 1, 1, 0] / 현재 풀이 값 = ", get_price_not_fall_periods(prices))
print("정답 = [6, 2, 1, 3, 2, 1, 0] / 현재 풀이 값 = ", get_price_not_fall_periods([3, 9, 9, 3, 5, 7, 2]))
print("정답 = [6, 1, 4, 3, 1, 1, 0] / 현재 풀이 값 = ", get_price_not_fall_periods([1, 5, 3, 6, 7, 6, 5]))