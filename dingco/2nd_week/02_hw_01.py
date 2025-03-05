class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self, value):
        self.head = Node(value)

    def append(self, value):
        cur = self.head
        while cur.next is not None:
            cur = cur.next
        cur.next = Node(value)
    # 0   1   2
    # 6 > 7 > 8
    # def get_kth_node_from_last(self, k):
    #     cur = self.head
    #     cnt = 0 # 전체 링크드리스트의 크기
    #     while cur is not None:
    #         cur = cur.next
    #         cnt += 1
    #     print(cnt)
    #     cur = self.head
    #     for _ in range(cnt-k):
    #         cur = cur.next
    #     return cur
# fast
# slow
# 투포인터 방법 : slow        fast 즉, slow 보다 k만큼 앞으로 보내고 같이 앞으로
    def get_kth_node_from_last(self, k):
        slow = self.head
        fast = self.head
        for i in range(k):
            fast = fast.next
        while fast is not None:
            fast = fast.next
            slow = slow.next
        return slow

linked_list = LinkedList(6)
linked_list.append(7)
linked_list.append(8)

print(linked_list.get_kth_node_from_last(2).data)  # 7이 나와야 합니다!