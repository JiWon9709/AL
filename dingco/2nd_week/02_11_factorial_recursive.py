# 수학공식을 최대한 써보기
# factorial(n) = n * factorial(n-1)
# factorial(n-1) = n-1 * factorial(n-2)
def factorial(n):
    if n == 1:
        return 1
    return factorial(n-1) * n


print(factorial(5))