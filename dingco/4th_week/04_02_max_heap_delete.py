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
        # [none, 8, 6, 7, 2, 5, 4]
        # 루트 노드와 마지막 노드 위치 바꾸기
        # [none, 4, 6, 7, 2, 5, 8]
        #    0   1  2  3  4  5  6
        self.items[1], self.items[-1] = self.items[-1], self.items[1]
        # 루트 노드 값 리턴값으로 저장
        prev_node = self.items.pop()
        # 변경된 루트 노드의 자식과 비교
        # 어디까지? 바닥까지
        cur_index = 1 # 루트노드 인덱스부터 시작
        while cur_index <= len(self.items):
            left_index = cur_index * 2
            right_index = cur_index * 2 + 1
            max_index = cur_index
            # 왼쪽노드와 오른쪽 노드 차례대로 비교해서
            if self.items[left_index] > self.items[max_index] and left_index < len(self.items):
                max_index = left_index
            if self.items[right_index] > self.items[max_index] and right_index < len(self.items):
                max_index = right_index
            if max_index == cur_index:
                break
            # 큰값과 교환
            self.items[max_index], self.items[cur_index] = self.items[cur_index], self.items[max_index]
        return prev_node


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