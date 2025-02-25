input = "011110"

# 0에서 1을 마주쳤을때 => 전체를 0으로 만들기 위한 작업
# 1에서 0을 마주쳤을때 => 전체를 1로 만들기 위한 작업
# 연속된 하나 이상의 숫자를 잡고 모두 뒤집기
def find_count_to_turn_out_to_all_zero_or_all_one(string):
    count_to_all_zero = 0
    count_to_all_one = 0
    # 맨 처음 숫자도 뒤집어 줘야함
    if string[0] == '0':
        count_to_all_one += 1
    elif string[0] == '1':
        count_to_all_zero += 1
    for i in range(len(string)-1): # i ~ 문자열의 길이 -2
        if string[i] != string[i+1]: # 옆자리 숫자가 같지 않을때
            if string[i+1] == "1":
                count_to_all_zero += 1
            if string[i+1] == "0":
                count_to_all_one += 1
    else:
        return min(count_to_all_zero, count_to_all_one)


result = find_count_to_turn_out_to_all_zero_or_all_one(input)
print(result)