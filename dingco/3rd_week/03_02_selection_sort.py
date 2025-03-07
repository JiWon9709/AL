input = [4, 6, 2, 9, 1]

def selection_sort(array):
    for i in range(len(array)):
        min = array[i]
        min_idx = i
        for j in range(i, len(array)):
            # 가장 작은수 찿기
            if min > array[j]:
                min = array[j]
                min_idx = j
        # 가장 작은 수를 찾아서 앞에서 순서대로 정렬
        array[min_idx] = array[i]
        array[i] = min
    return array

selection_sort(input)
print(input) # [1, 2, 4, 6, 9] 가 되어야 합니다!

print("정답 = [1, 2, 4, 6, 9] / 현재 풀이 값 = ",selection_sort([4, 6, 2, 9, 1]))
print("정답 = [-1, 3, 9, 17] / 현재 풀이 값 = ",selection_sort([3,-1,17,9]))
print("정답 = [-3, 32, 44, 56, 100] / 현재 풀이 값 = ",selection_sort([100,56,-3,32,44]))