import sys 
from collections import Counter
N = int(input()) 
arr = list(map(int, (sys.stdin.readline().split())))

def is_goodarr(arr):
    # 각 원소의 등장 횟수를 세기
    counts = Counter(arr)
    
    # 각 원소의 등장자리를 저장하기 위한 빈 딕셔너리 생성
    indices = {value: [] for value in counts.keys()}
    
    # 각 원소의 등장한 자리와 원소값을 저장하기기
    for idx, value in enumerate(arr):
        indices[value].append(idx)
    
    # 원소값과 등장한 자리를 비교
    for value, pos in indices.items():
        # a_i = a_p 전제 조건이면
        i, p = pos
        for other_value, other_pos in indices.items():
            # 다른 값과 비교
            if other_value != value:
                j, q = other_pos # a_j = a_q이므로 NO
                if i < j < p < q:
                    return print("NO")
    return print("YES")
    
is_goodarr(arr)