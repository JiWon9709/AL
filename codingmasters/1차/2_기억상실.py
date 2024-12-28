import sys 

a, b, n = map(int, sys.stdin.readline().split())

w_day = a-b # 하루동안 외운것(1일 이상일 경우, 막날 빼고)
day = (n-a) // w_day + 1 # 마지막날은 a개를 외움
    
print(day)