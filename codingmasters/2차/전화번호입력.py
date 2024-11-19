import sys 

S = sys.stdin.readline().strip()

def is_tel(S):
    if len(S) != 13:
        return print("invalid")
    else:
        if S[:4] == "010-":
            S = S[4:]
        else:
            return print("invalid")
        for i, s in enumerate(S):
            if i == 4 and s != '-':
                return print("invalid")
            if i !=4 and not(int(s) >= 0 and int(s) <= 9):
                return print("invalid")
        return print("valid")
    # # 좀더 깔끔한 버전 ,길이와 형식 검증
    # if len(S) == 13 and S[:4] == "010-" and S[8] == "-" and S[4:8].isdigit() and S[9:].isdigit():
    #     print("valid")
    # else:
    #     print("invalid")
is_tel(S) 