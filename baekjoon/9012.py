# 1. flag 생각하다가 짝이 맞고 ((())) 여러개 겹칠때가 생각하기 어려워서
# 2. stack 자료구조로 더 간단하게 할수있다는것을 깨달았다.
# (가 들어올때 넣어두다가 )가 들어오면 하나씩 빼주기
t = int(input())
arr = []
for _ in range(t):
    arr.append(input())

for ps in arr:
    s = [] # stack
    
    for i in range(len(ps)):
        if ps[i] == '(':
            s.append('(')
        elif ps[i] == ')':
            if s:
                s.pop(-1)
            else:
                print('NO')
                break
        else:
            next
            
    else:
        if s:
            print('NO')
        else:     
            print('YES')

