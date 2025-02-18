def find_max_num(array):
    # 이 부분을 채워보세요!
    # i = max(array)
    max = array[0]
    for i in array:
        if max < i:
            max = i
    return max

# 아이디어를 한번 글로써보고 코딩
print("정답 = 6 / 현재 풀이 값 = ", find_max_num([3, 5, 6, 1, 2, 4]))
print("정답 = 6 / 현재 풀이 값 = ", find_max_num([6, 6, 6]))
print("정답 = 1888 / 현재 풀이 값 = ", find_max_num([6, 9, 2, 7, 1888]))