# 투포인터?
    # ( ( ) ) ( )
    # ^   ^
    # 0 1 2 3 4 5
    # 0. 괄호가 열렷다
    # 1. 괄호가 열렷다
    # 2. 1번째의 괄호가 닫혓다
    # 3. 0번째의 괄호가 닫힘
    # 4. 열림
    # 5. 4번째의 괄호가 닫힘
    # )가 나오면 가장 최근에 나온 (을 빼줘야함.
# stack
def is_correct_parenthesis(string):
    # left_idx = 0
    # right_idx = 0
    # print(string)
    #                  # 0         5
    # for i in range(left_idx, len(string)):
    #     print(left_idx, right_idx)
    #     if string[i] == '(':
    #         left_idx = i
    #                        # 2          5
    #     for j in range(right_idx+1, len(string)):
    #         if string[j] == ')':
    #             right_idx = j
    #             break
    #     # left > right 이면 false
    #     if left_idx >= right_idx:
    #         return False
    stack = []
    for str in string:
        if str == '(':
            stack.append(str)
        else:
            if stack:
                stack.pop()
            else:
                return False
    if stack: return False
    else:
        return True


print("정답 = True / 현재 풀이 값 = ", is_correct_parenthesis("(())"))
print("정답 = False / 현재 풀이 값 = ", is_correct_parenthesis(")"))
print("정답 = False / 현재 풀이 값 = ", is_correct_parenthesis("((())))"))
print("정답 = False / 현재 풀이 값 = ", is_correct_parenthesis("())()"))
print("정답 = False / 현재 풀이 값 = ", is_correct_parenthesis("((())"))