class MaxHeap:
    def __init__(self):
        self.items = [None]

    def insert(self, value):
        self.items.append(value)
        cur_index = len(self.items) - 1

        while cur_index > 1:  # cur_index 가 1이 되면 정상을 찍은거라 다른 것과 비교 안하셔도 됩니다!
            parent_index = cur_index // 2
            if self.items[parent_index] < self.items[cur_index]:
                self.items[parent_index], self.items[cur_index] = self.items[cur_index], self.items[parent_index]
                cur_index = parent_index
            else:
                break

    def delete(self):
        # 가장 맨위의 값과 마지막 값을 교환
        self.items[1], self.items[-1] = self.items[-1], self.items[1]
        # 마지막값 삭제
        prev_max = self.items.pop()
        # 다시 정렬 부모 -> 자식 비교해야하기 때문에 루트에서 시작
        cur_idx = 1
        # 바닥에 도달할때까지 루프
        while cur_idx <= len(self.items) - 1:
            left_child_idx = cur_idx * 2
            right_child_idx = cur_idx * 2 + 1
            # 두 자식중 큰 노드와 자리를 바꿔야함
            max_idx = cur_idx
            if left_child_idx <= len(self.items)-1 and self.items[left_child_idx] > self.items[max_idx]:
                max_idx = left_child_idx
            if right_child_idx <= len(self.items)-1 and self.items[right_child_idx] > self.items[max_idx]:
                max_idx = right_child_idx
            # 자식노드보다 크면 바뀌지 않으므로 루프 탈출
            if max_idx == cur_idx:
                break
            # 자식노드 중 큰 값과 자리 바꿈
            self.items[cur_idx], self.items[max_idx] = self.items[max_idx], self.items[cur_idx]
            # 다시 현재노드의 idx값을 바꿔줌.
            cur_idx = max_idx
        return prev_max  # 8 을 반환해야 합니다.


max_heap = MaxHeap()
max_heap.insert(8)
max_heap.insert(6)
max_heap.insert(7)
max_heap.insert(2)
max_heap.insert(5)
max_heap.insert(4)
print(max_heap.items)  # [None, 8, 6, 7, 2, 5, 4]
print(max_heap.delete())  # 8 을 반환해야 합니다!
print(max_heap.items)  # [None, 7, 6, 4, 2, 5]