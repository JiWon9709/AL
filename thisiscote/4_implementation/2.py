knight = list(input())
chess = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
for i, val in enumerate(chess):
    if knight[0] == val:
        wid = i
        break
dx = [-2, -2, 2, 2, 1, -1, 1, -1]
dy = [1, -1, 1, -1, 2, 2, -2, -2]
x, y = wid, int(knight[1])-1
result = 0
for i in range(8):
    x, y = wid, int(knight[1])-1
    x += dx[i]
    y += dy[i]
    if x < 8 and x >= 0 and y < 8 and y >= 0:
        result += 1
print(result)
    