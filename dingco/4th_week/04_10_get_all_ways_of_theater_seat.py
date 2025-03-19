seat_count = 9
vip_seat_array = [4, 7]

# 점화식
# n 번째 좌석에 앉는 경우
# 1. n 번째 좌석에 앉거나
# -> n-1 개 남아있고, 사람도 n-1 번째 티켓까지 가진 사람이 있는 상황
# 2. n-1 번째 좌석에 앉거나
# n-1 번째 티켓을 가진 사람은 n번째 좌석에 앉아야만 함
# 즉 피보나치 수열...
memo = {1: 1,
        2: 2}
def fibo(i, memo):
    if i in memo:
        return memo[i]
    n = fibo(i-1, memo) + fibo(i-2, memo)
    memo[i] = n
    return n

def get_all_ways_of_theater_seat(total_count, fixed_seat_array):
    cnt = 1
    cur = 0
    # totalcount 만큼의 자리 생성
    seat_array = [0] * total_count
    for i in range(total_count):
        if i+1 in fixed_seat_array:
            # seat_array[i] = i
            cnt *= fibo(cur, memo)
            cur = 0
            continue
        cur += 1
    cnt *= fibo(total_count - (fixed_seat_array[-1]), memo)
    # 1 2 3 4 5 6 7
    # 1 2 3 5 8

    # 양옆의 자리만 가능
    # 0 1 2 3 4 5 6 7 8
    #       3     6
    # 0 1 2
    # 1 0 2
    # 0 2 1
    #         4 5   7 8
    #         5 4   8 7
    # 3 * 2 * 2
    # 0 1 2 3 4 5 6
    #           5     0   1 2  3 4 5 6
    # 0 1 2 3 4       0 - 1-3 -2-4
    #                      -2 -3-4
    #                         -4-3
    # 0 1 2 4 3         - 2-1 -3-4
    #                         -4-3
    # 0 1 3 2 4       1 - 0-2 -3-4
    #                         -4-3
    #                      -3 -2-4
    # 0 2 1 3 4
    # 0 2 1 4 3
    # 1 0 2 3 4
    # 1 0 2 4 3
    # 1 0 3 2 4
    return cnt


# 12가 출력되어야 합니다!
print(get_all_ways_of_theater_seat(seat_count, vip_seat_array))

print("정답 = 4 / 현재 풀이 값 = ", get_all_ways_of_theater_seat(9,[2,4,7]))
print("정답 = 26 / 현재 풀이 값 = ", get_all_ways_of_theater_seat(11,[2,5]))
print("정답 = 6 / 현재 풀이 값 = ", get_all_ways_of_theater_seat(10,[2,6,9]))