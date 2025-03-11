# 1. 장르 별로 재생횟수를 모두 모아서 비교
# 특정 키 값에 대해서 value를 모아서 합쳐주고싶다.
# 2. 장르 내에서 많이 재생된 노래를 먼저 수록
# (index, 재생횟수)
# 딕셔너리 dict2= {"classic" : [(0, 500), (2, 150), (3, 800)]}
#
def get_melon_best_album(genre_array, play_array):
    dict1 = {} # total
    dict2 = {} # index
    n = len(genre_array)
    for i in range(n):
        if genre_array[i] in dict1:
            dict1[genre_array[i]] += play_array[i]
            dict2[genre_array[i]].append((i, play_array[i]))
        else:
            dict1[genre_array[i]] = play_array[i]
            dict2[genre_array[i]] = [(i, play_array[i])]

    result = []
    sorted_genre_play_arr = sorted(dict1.items(), key=lambda item: item[1], reverse=True)
    for genre, total_play in sorted_genre_play_arr:
        sorted_genre_index_arr = sorted(dict2[genre], key=lambda item: item[1], reverse=True)
        genre_count = 0
        for index, play in sorted_genre_index_arr:
            if genre_count >= 2:
                break
            result.append(index)
            genre_count += 1
    return result


print("정답 = [4, 1, 3, 0] / 현재 풀이 값 = ", get_melon_best_album(["classic", "pop", "classic", "classic", "pop"], [500, 600, 150, 800, 2500]))
print("정답 = [0, 6, 5, 2, 4, 1] / 현재 풀이 값 = ", get_melon_best_album(["hiphop", "classic", "pop", "classic", "classic", "pop", "hiphop"], [2000, 500, 600, 150, 800, 2500, 2000]))