import sys 

x, y, z = map(int, (sys.stdin.readline()).split())

# 두 기차가 충돌할때까지 시간을 구해서
# 파리가 나는 거리 = z * (x / 2 * y)

print(int(z * (x / (2 *y))))