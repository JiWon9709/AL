def summarize_string(input_str):
    # 알파벳 빈도수 세기
    count_alphabet = [0] * 26
    for char in input_str:
        count_alphabet[ord(char) - ord('a')] += 1

    # 알파벳 종류와 갯수 요약해서 출력
    # count_alphabet > 0
    result_str = []
    for idx in range(len(count_alphabet)):
        if count_alphabet[idx] > 0:
            result_str.append(chr(idx+97)+str(count_alphabet[idx]))
            # now += 1

    return "/".join(result_str)


input_str = "acccdeee"

print(summarize_string(input_str))