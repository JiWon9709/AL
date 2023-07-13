# 2309_07_12
height = [int(input()) for i in range(9)] # 9명 입력
height.sort() # 오름차순 정렬
# 7명 다 합치면 100이여야하니까 빠져야할 2명의 몸무게합
height_sum = sum(height) - 100

# 빠져야할 두명 찾기
for i in range(0, 9):
    for j in range(i+1, 9):
        if height[i] + height[j] == height_sum:
            tmp1 = height[i]
            tmp2 = height[j]

height.remove(tmp1)
height.remove(tmp2)

for i in height:
    print(i)