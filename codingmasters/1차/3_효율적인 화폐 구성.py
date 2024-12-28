import sys 

n, m = map(int, (sys.stdin.readline().split())) 
coin_kind = [int(sys.stdin.readline()) for _ in range(n)]

# 동적계획법으로도 풀수 있음
# # DP 테이블 초기화 
# dp = [float('inf')] * (M + 1)  # 금액 M까지의 최소 동전 개수 기록 (초기값은 무한대) 
# dp[0] = 0  # 금액 0을 만드는 데 필요한 동전 개수는 0개 
 
# # 동적 계획법(DP) 수행 
# for coin in coins: 
#     for amount in range(coin, M + 1): 
#         # 현재 금액을 만들기 위한 최소 동전 개수를 갱신 
#         dp[amount] = min(dp[amount], dp[amount - coin] + 1) 
 
# # 결과 출력 
# if dp[M] == float('inf'): 
#     print(-1)  # M을 만들 수 없는 경우 
# else: 
#     print(dp[M])  # M을 만들기 위한 최소 동전 개수 

def cal_coin(n, m, coin_kind):
    # 동전 정렬
    coin_kind.sort(reverse=True)
    total = 0
    for coin in coin_kind:
        if m == 0:
            break
        count = m // coin
        total += count
        m -= count*coin
    return total if m == 0 else -1

# 최소 동전의 개수
count = cal_coin(n, m, coin_kind)
print(count)