input = "abcba"

# 맨처음과 맨마지막 비교
# 가운데는 상관없음

# def is_palindrome(string):
#     tail = len(string) - 1
#     head = 0
#     while tail > head:
#         if string[head] != string[tail]:
#             return False
#         head += 1
#         tail -= 1
#     return True

def is_palindrome(string):
    if string[0] != string[-1]:
        return False
    if len(string) <= 1:
        return True
    return is_palindrome(string[1:-1])

print(is_palindrome(input))