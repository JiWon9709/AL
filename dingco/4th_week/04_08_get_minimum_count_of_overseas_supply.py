import heapq

# ramen_stock = 4
# supply_dates = [4, 10, 15]
# supply_supplies = [20, 5, 10]
# supply_recover_k = 30


def get_minimum_count_of_overseas_supply(stock, dates, supplies, k):
    # dates [4 10 15]
    # sup   [20 5 10]
    cnt = 0
    max_heap = []
    last_day_index = 0
    # 밀가루가 떨어지지 않고 /공장을 운영하기 위해서
    # 최소한 몇번 공장으로부터 밀가루를 공급받아야하는지
    while stock <= k:
        # 재고량이 버틸수 있는 날까지 해당되는 모든 날짜를 힙에 넣기
        while last_day_index < len(dates) and dates[last_day_index] <= stock:
            heapq.heappush(max_heap, supplies[last_day_index] * -1)
            last_day_index += 1
        print(max_heap)
        # 힙에서 최댓값을 뽑기
        heap_pop = heapq.heappop(max_heap) * -1
        stock += heap_pop # 다시 재고량에 추가해서 while문으로
        cnt += 1
    return cnt

    #------- 아래코드는 오류가 있음. 최솟값을 못구함
    # cur_stock = stock
    # k 일까지 최소한 몇번 공급을 받아야하는지
    # 최소한으로 공급 받으면, 공급량이 큰 수대로 받아야함.
    # 공급 가능 날마다 체크
    # for i, day in enumerate(dates):
    #     print("day=", day,"cur_stock", cur_stock)
    #     # 날마다 현재 밀가루량 체크
    #     # day 때문에 현재 남은량 다 더해주기
    #     # cur_stock = cur_stock - day # 4 - 4 = 0
    #     # 최소 필요한 개수 = 날짜마다 현재 날에서 남아있는 재고를 빼기.
    #     min_stock = k - cur_stock # 30 - 0 = 30
    #     if cur_stock >= k:
    #         break
    #     # 재고량이 0 / 다음 날짜까지 못버티면 /총 k일까지 못버틴다/ 공급받아야함.
    #     #                       30         20
    #     if cur_stock - day == 0 or min_stock >= supplies[i]:
    #         cnt += 1
    #         cur_stock += supplies[i] # 20
    # return cnt


# print(get_minimum_count_of_overseas_supply(ramen_stock, supply_dates, supply_supplies, supply_recover_k))
print("정답 = 2 / 현재 풀이 값 = ", get_minimum_count_of_overseas_supply(4, [4, 10, 15], [20, 5, 10], 30))
print("정답 = 4 / 현재 풀이 값 = ", get_minimum_count_of_overseas_supply(4, [4, 10, 15, 20], [20, 5, 10, 5], 40))
print("정답 = 1 / 현재 풀이 값 = ", get_minimum_count_of_overseas_supply(2, [1, 10], [10, 100], 11))