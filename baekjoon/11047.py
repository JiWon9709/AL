# greedy 알고리즘: 매 선택에서 지금 최적인 답을 선택해 적합한 결과를 도출하는 알고리즘
# A1 = 1, i ≥ 2인 경우에 Ai는 Ai-1의 배수 <= 조건때문에 greedy 알고리즘 가능
n, k = map(int, input().split())
pocket = [int(input()) for _ in range(n)]
cnt = 0
for i in range(n-1, -1, -1):
    if k >= pocket[i]:
        cnt = cnt + int(k // pocket[i])
        k = k - int(k // pocket[i]) * pocket[i]
print(cnt)