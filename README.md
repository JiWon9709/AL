# AL = Algorithm

- 언어: python
# [1주차] 시간 복잡도 & 공간 복잡도
- 시간 복잡도 : 입력값(N)에 비례해서 어느 정도로 증가하는지 파악
- 공간 복잡도 : 대부분의 문제에서는 알고리즘의 성능이 공간에 의해 결정x, but N^2, N^3 일 경우는 달라질수 있다.
- 점근 표기법
-   빅오(O(N)) 표기법 : 최악의 성능이 나올때 어느 정도의 연산량이 나올지 표기
-   빅오메가(Ω(1)) 표기법 : 최선의 성능이 나올때 어느 정도의 연산량이 나올지 표기

# [2주차] Array & LinkedList
- Array vs LinkedList
- 특정 원소 찾기 용이 | 삽입, 삭제 용이
- 클래스로 Node 와 LinkedList 를 생성해서 append, delete, get_node 함수 생성
- 순열 문제가 나왔을때는 tail 속성도 추가해주면 사용하기 용이
- 이진 탐색 : 정렬이 된 리스트를 이진 탐색
- 재귀함수 : 탈출 조건이 있어야함.

  
# [3주차] 정렬, 스택, 큐, 해시
- 버블정렬, 선택정렬, 삽입정렬,
- 합병정렬: 문제를 매우 작게 쪼개어서 해결하고 merge
- 스택 : LIFO 마지막에 들어간게 가장먼저 out, list 로 구현
- 큐: FIFO 선입선출, enqueue, dequeue, from collections import deque, popleft
- 해시
