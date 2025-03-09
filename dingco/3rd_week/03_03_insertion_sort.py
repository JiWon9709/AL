input = [4, 6, 2, 9, 1]
#     1
# [4, 6, 2, 9, 1]
#     1  2
# [4, 6, 2, 9, 1]
# 1 -> 2, 1 -> 3, 2, 1 ->

def insertion_sort(array):
    n = len(array)
    # O(N^2)
    # O(N)
    # 인덱스 1부터 시작. 새로운 신병이 들어왔을때, 전값과 비교
    for i in range(1, n):
        for j in range(i):
            if array[i - j] < array[i - j - 1]:
                tmp = array[i - j - 1]
                array[i-j-1] = array[i - j]
                array[i-j] = tmp
            else: # 앞부분은 정렬이 되어있기때문에 넘겨도됌.
                break
    return array


insertion_sort(input)
print(input) # [1, 2, 4, 6, 9] 가 되어야 합니다!

print("정답 = [4, 5, 7, 7, 8] / 현재 풀이 값 = ",insertion_sort([5,8,4,7,7]))
print("정답 = [-1, 3, 9, 17] / 현재 풀이 값 = ",insertion_sort([3,-1,17,9]))
print("정답 = [-3, 32, 44, 56, 100] / 현재 풀이 값 = ",insertion_sort([100,56,-3,32,44]))