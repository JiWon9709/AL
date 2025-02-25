# 빅오 -> 최악
# 빅오메가 -> 최선
def is_number_exist(number, array):
    # 이 부분을 채워보세요!
    for number_array in array: # array의 길이만큼 아래 연산이 실행
        if number == number_array: # 비교 연산 1번 실행
            return True # 시간복잡도 = N
    return False


result = is_number_exist
print("정답 = True 현재 풀이 값 =", result(3, [3,5,6,1,2,4]))
print("정답 = Flase 현재 풀이 값 =", result(7, [6,6,6]))
print("정답 = True 현재 풀이 값 =", result(2, [6,9,2,7,1888]))