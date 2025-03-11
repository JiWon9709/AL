shop_prices = [30000, 2000, 1500000]
user_coupons = [20, 40]

# 스택, 큐, 딕셔너리
def get_max_discounted_price(prices, coupons):
    prices.sort(reverse=True)
    coupons.sort(reverse=True)
    res = 0
    # price, coupon
    # 일반적으로 제일 큰 가격에 큰 퍼센트의 쿠폰을 할인 받으면 되는것 아닌가?
    # 30 20
    # 200000 10000 5000
    if len(coupons) < len(prices):
        for i in range(len(coupons)):
            res += prices[i] * (100 - coupons[i])/100
        for j in range(len(coupons), len(prices)):
            res += prices[j]
    else: # 쿠폰의 개수가 가격수보다 클때
        # 50 40 30 20
        # 10000 5000
        for i in range(len(prices)):
            res += prices[i] * (100 - coupons[i]) / 100

    return res


print("정답 = 926000 / 현재 풀이 값 = ", get_max_discounted_price([30000, 2000, 1500000], [20, 40]))
print("정답 = 485000 / 현재 풀이 값 = ", get_max_discounted_price([50000, 1500000], [10, 70, 30, 20]))
print("정답 = 1550000 / 현재 풀이 값 = ", get_max_discounted_price([50000, 1500000], []))
print("정답 = 1458000 / 현재 풀이 값 = ", get_max_discounted_price([20000, 100000, 1500000], [10, 10, 10]))