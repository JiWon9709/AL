import sys 

n, k = map(int, sys.stdin.readline().split())

arr = sys.stdin.readline()
for i in range(len(arr)):
    for j in range(k):
        print(arr[i],end='')