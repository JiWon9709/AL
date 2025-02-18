def find_max_occurred_alphabet(string):
    count_arr = find_alphabet_occurrence_array(string)
    # 이 부분을 채워보세요!
    max_arr = 0
    for index in range(len(count_arr)):
        if count_arr[index] > count_arr[max_arr]:
            max_arr = index
    return chr(max_arr+97)

# 알파벳 빈도수
def find_alphabet_occurrence_array(string):
    alphabet_occurrence_array = [0] * 26

    for char in string:
        if char.isalpha():
            idx = ord(char) - ord('a')
            alphabet_occurrence_array[idx] += 1
    return alphabet_occurrence_array


print("정답 = [1, 0, 2, 2, 2, 0, 2, 1, 3, 0, 0, 2, 2, 3, 3, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0] \n현재 풀이 값 =",
      find_alphabet_occurrence_array("hello my name is dingcodingco"))
print("정답 = [1, 0, 0, 0, 2, 0, 1, 1, 1, 0, 0, 2, 1, 0, 2, 0, 0, 1, 0, 1, 0, 1, 1, 0, 0, 0] \n현재 풀이 값 =",
      find_alphabet_occurrence_array("we love algorithm"))
print("정답 = [0, 3, 0, 0, 3, 1, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 2, 3, 2, 0, 0, 0, 1, 0] \n현재 풀이 값 =",
      find_alphabet_occurrence_array("best of best youtube"))

# 아스키코드를 활용해서 ord('a') = 97
# ord('a') - 97 = 0
# chr(97) = 'a'
# 알파벳이 없으면 alphabet_arr 배열에 추가
# 알파벳이 있으면 count_arr +1

result = find_max_occurred_alphabet
print("정답 = i 현재 풀이 값 =", result("hello my name is dingcodingco"))
print("정답 = e 현재 풀이 값 =", result("we love algorithm"))
print("정답 = b 현재 풀이 값 =", result("best of best youtube"))