g = int(input()) # 게이트
p = int(input()) # 비행기 수

gate_info = [0] * (g+1) # 부모 테이블

# 부모테이블의 자기자신 초기화
for i in range(g+1):
    gate_info[i] = i

# 재귀적으로 호출해서 특정 원소가 속한 집합 찾기
def find_parent(parent, i):
    if parent[i] != i:
        parent[i] = find_parent(parent, parent[i])
    return parent[i]

# 두 원소가 속한 집합 합치기
def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b
      
result = 0
# 비행기마다 도킹 할수있는지 체크
for _ in range(p):
    data = find_parent(gate_info, int(input())) # 현재 루트
    if data == 0: # 현재 루트가 0이면 종료
        break
    # 그렇지 않다면 왼쪽의 집합과 합치기
    union_parent(gate_info, data, data-1)
    result += 1

print("결과: ", result)