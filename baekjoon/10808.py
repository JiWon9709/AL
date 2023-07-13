# 10808
import sys

# s = sys.stdin.readline().rstrip()
# alpabet = [0] * (26) #알파벳 26개
#
# for i in s:
#     alpabet[ord(i) - 97] += 1
# for i in range(len(alpabet) - 1):
#     print(alpabet[i], end=" ")

# 딕셔너리 사용 / {key, value}
s = input()
d = {}
for i in 'abcdefghijklmnopqrstuvwxyz':
    d[i] = 0
for i in s:
    if i in d:
        d[i] += 1
for i in d.values():
    print(i, end=" ")