input = 20


def find_prime_list_under_number(number):
    arr_prime = []
    # 정수를 입력했을때 이하의 소수를 모두 반환
    for prime in range(2, number+1):
        # 1번 방법
        # for i in range(2, prime):
        # 2번 방법
        # n 보다 작은 모든 소수에 대해서
        # 3번 방법: N의 제곱근보다 크지 않은 어떤 소수로도 나누어 떨어지지 않는다.
        print(arr_prime)
        for i in arr_prime:
            if i * i <= prime and prime % i == 0: # 나누어 떨어지면 소수가 아님
                break
        else:
            # 모든 for문을 돌고 나오면 소수
            arr_prime.append(prime)
    return arr_prime


result = find_prime_list_under_number(input)
print(result)