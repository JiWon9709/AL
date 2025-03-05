shop_menus = ["만두", "떡볶이", "오뎅", "사이다", "콜라"]
shop_orders = ["오뎅", "콜라", "만두", "순대"]


def is_available_to_order(menus, orders):
    # 시간복잡도 O(N*logN) + O(M) * O(log(N))
    # menus.sort()
    # for order in orders:
    #     if not is_available(menus, order): # 메뉴가 없으면 False
    #         return False
    # return True

    # O(N) + O(M) * O(1)  = O(N + M)
    menus_set = set(menus) # O(N)
    for order in orders: # O(M)
        if order not in menus_set: # O(1)
            return False
    return True

def is_available(menus, order):
    cur_min = 0
    cur_max = len(menus) -1
    cur_guess = (cur_min + cur_min) // 2
    while cur_min <= cur_max:
        print(menus[cur_guess])
        if menus[cur_guess] == order:
            return True
        elif menus[cur_guess] < order:
            cur_min = cur_guess + 1
        else:
            cur_max = cur_guess - 1
        cur_guess = (cur_min + cur_min) // 2
    return False


result = is_available_to_order(shop_menus, shop_orders)
print(result)