n = int(input())
lst = list(input().split())
tb = [[0] * (n+1) for _ in range(n+1)]
start_x, start_y = 1, 1
for i in lst:
    if i == 'L':
        start_y -= 1
        if start_y < 1 or start_y > n+1:
            start_y += 1
    elif i == 'R':
        start_y += 1
        if start_y < 1 or start_y > n+1:
            start_y -=1
    elif i == 'U':
        start_x -= 1
        if start_x < 1 or start_x > n+1:
            start_x += 1
    else:
        start_x += 1
        if start_x < 1 or start_x > n+1:
            start_x -=1
print(start_x, start_y)
        
