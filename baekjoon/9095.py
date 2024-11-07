# 1. from itertools import combinations 조합, 순열을 써보려고 했으나 답이 이상함
# 2. dp로 다시해보기
n = int(input())
arr = [int(input()) for _ in range(n)]
# 뒤에 추가되는 부분이 1이 몇개인지, 2가 몇개인지, 3이 몇개인지 새어보면
# 각각 f(n-1)개, f(n-2) 개, f(n-3) 개가 된다는것을 알수있다.
# Ex) n = 4 일때 f(3) + 1 = 4 / f(2) + 2 = 2 / f(1) + 3 = 1
# ex) n = 5 일때 f(4) + 1 = 7 / f(3) + 2 = 4 / f(2) + 3 = 2
# 즉 점화식은 f(n) = f(n-1) + f(n-2) + f(n-3)
def f(x):
    if x == 1: # 1
        return 1
    elif x == 2: # 1+1, 2
        return 2
    elif x == 3: # 1+1+1, 1+2, 2+1, 3
        return 4
    else:
        return f(x-1) + f(x-2) + f(x-3)
# -----------------------------
# def represent_n(t, r):
#     cnt = 0
#     # pre = []
#     # if (t % r)==0:
#     #     cnt+=1
#     if (t // r) >=1:
#         for i in range(1, int(t//r)+1):
#             if i * r == t:
#                 cnt += 1
#             else:
#                 pre = (t-(i*r))*[1] + i*[r]# 1의 개수 + i = 전체개수
#                 cnt += len(list(combinations(pre, i)))
#             print(pre)    
#     return (cnt)
#----------------------------------------
for t in arr:
    # sum = 0
    # sum += represent_n(t, 3)
    # print('3 : ',represent_n(t, 3))
    
    # sum += represent_n(t, 2)
    # print('2 : ',represent_n(t, 2))
    # #represent_n(t, 1) # 항상 1
    # print(sum+1)
    # -----------------------------
    print(f(t))