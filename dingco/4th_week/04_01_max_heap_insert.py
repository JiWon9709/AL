class MaxHeap:
    def __init__(self):
        self.items = [None]

    def insert(self, value):
        # 맨뒤에 노드 추가
        self.items.append(value)
        # [None, value]
        # if len(self.items) == 2: # 노드 하나있을때
        #     return
        # 부모노드와 비교해서 부모보다 클때, 부모와 위치 변경
        present_idx = len(self.items) - 1
        while present_idx != 1: # 1인 경우에는 루트노드
            parent_idx = (present_idx) // 2
            if self.items[parent_idx] < self.items[present_idx]:
                self.items[parent_idx] , self.items[present_idx] = self.items[present_idx], self.items[parent_idx]
                present_idx = parent_idx
            else:
                break

#     0    level 0
#   6   3  level 1
# 4  2 5   level 2

max_heap = MaxHeap()
max_heap.insert(3)
# 3   level 0
# [none, 3]
max_heap.insert(4)
#  3
# 4
# 맨뒤에 넣고 부모와 비교
# [none, 4, 3]
max_heap.insert(2)
#  4
# 3 2
max_heap.insert(9)
#   4
#  3 2
# 9
print(max_heap.items)  # [None, 9, 4, 2, 3] 가 출력되어야 합니다!