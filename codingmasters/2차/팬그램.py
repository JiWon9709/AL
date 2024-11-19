import sys 
# 팬그램 : 모든 알파벳을 사용해 문장을 만든 것
p = list(sys.stdin.readline().strip()) 
alp = [0] * 26

def check_alp(a):
    if ord(a) >= 97:
        # 65~90: 대문자26 / 97~122 : 소문자26
        alp[ord(a)-97] = 1
    else:
        alp[ord(a)-65] = 1

for x in range(len(p)):
    check_alp(p[x])

if 0 in alp:
    print('NO')
else:
    print('YES')
