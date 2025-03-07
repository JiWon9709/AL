numbers = [1, 1, 1, 1, 1]
target_number = 3

# 더하거나 빼기를 통해 타겟숫자로 바꾸기
# 1 1 1 1 1
# 1, 3, 5 은 가능 , 2, 4는 불가능
# (-1, +1) 한세트는 0을 만들수 있다.
# +1 +1 (+1 -1) +1

# [2, 3, 1]
# 0
# +2 +3 +1
# +2 +3 -1
# +2 -3 +1
# -2 +3 +1
# -2 -3 +1
# -2 +3 -1
# +2 -3 -1
# -2 -3 -1
# 모든 경우의 수를 써봐야함
result = [] # 모든 경우의 수
def get_count_of_ways_to_target_by_doing_plus_or_minus(array, target):
    get_all_ways_by_doing_plus_or_minus(array, 0, 0)
    # return 5

def get_all_ways_by_doing_plus_or_minus(array, current_index, current_sum):
    if current_index == len(array):
        result.append(current_sum)
        return
    get_all_ways_by_doing_plus_or_minus(array, current_index+1, current_sum+array[current_index])
    get_all_ways_by_doing_plus_or_minus(array, current_index+1, current_sum-array[current_index])


get_count_of_ways_to_target_by_doing_plus_or_minus(numbers, target_number)
print(result)  # 5를 반환해야 합니다!
cnt = 0
for res in result:
    if res == target_number:
        cnt += 1
print(cnt)