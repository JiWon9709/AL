# 2 * N 개의 방
N = int(input())

rooms = [0] * (N+1)

# dp : 바텀업 방식
rooms[0], rooms[1], rooms[2] = 0, 3, 7
for i in range(3, N+1):
    rooms[i] = (rooms[i-1] * 2 + rooms[i-2]) % 796796

print(rooms[N])