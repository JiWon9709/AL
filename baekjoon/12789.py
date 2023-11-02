import sys

n = int(sys.stdin.readline())
a = list(map(int, sys.stdin.readline().split()))
stack = []
target = 1

# 1번째로 생각한 아이디어 = 배열 분리하는 함수로 만들기
# # a = 현재 줄서있는 배열, x = 간식받는 순서 1부터~n까지
# # return 남아 있는 줄
# def get_line(a, x):
#     i = 0
#     if len(a) != 0:
#         while a[i] != x:
#             stack.append(a[i])
#             i += 1
#         del a[i]
#         b = a[i:]
#     else:
#         return stack
#     return b
# for t in range(1, n+1):
#     a = get_line(a, t)
#     # print(i)
#     t += 1

# pop(0) 맨앞 꺼내기 // pop() 맨뒤 꺼내기
# target을 1~n까지 찾기
# 줄 서있는 애들이 있는동안
while a:
    # 맨앞에 서있는애가 target이면 pop하고 target +1
    if a[0] == target:
        a.pop(0)
        target +=1
    else:
        stack.append(a.pop(0))
    # stack에 애들이 있다면 맨 뒤에 학생부터 확인
    while stack:
        if stack[-1] == target:
            stack.pop()
            target += 1
        else:
            break
if not stack:
    print('Nice')
else:
    print('Sad')