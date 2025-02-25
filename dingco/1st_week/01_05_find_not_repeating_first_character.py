input = "abadabac"

# 알파벳 빈도수
def find_alphabet_occurrence_array(string):
    alphabet_occurrence_array = [0] * 26

    for char in string:
        if char.isalpha():
            idx = ord(char) - ord('a')
            alphabet_occurrence_array[idx] += 1
    return alphabet_occurrence_array

def find_not_repeating_first_character(string):
    # 반복되는지 아닌지를 판단
    # string 에서 알파벳의 빈도수를 찾는다.
    occurrence_array = find_alphabet_occurrence_array(string)
    # 빈도수가 1인 알파벳 중 string에서 뭐가 먼저 나왔는지를 찾아본다.
    not_repeating_character_array = []
    for idx in range(len(occurrence_array)):
        if occurrence_array[idx] == 1:
            not_repeating_character_array.append(chr(idx+97))
    # print(not_repeating_character_array)
    for find_first in string:
        if find_first in not_repeating_character_array:
            return find_first
    return "_"


result = find_not_repeating_first_character
print("정답 = d 현재 풀이 값 =", result("abadabac"))
print("정답 = c 현재 풀이 값 =", result("aabbcddd"))
print("정답 =_ 현재 풀이 값 =", result("aaaaaaaa"))