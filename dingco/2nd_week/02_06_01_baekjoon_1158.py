# BOJ 1158
class Node():
    def __init__(self, value):
        self.data = value
        self.next = None

class LinkedList():
    def __init__(self, value):
        node = Node(value)
        self.head = node
        # 원형 리스트를 위해 tail 노드 관리
        self.tail = node
        self.tail.next = self.head

    def append(self, value):
        new_node = Node(value)
        self.tail.next = new_node
        self.tail = new_node
        self.tail.next = self.head

    def get_node(self, index):
        cur = self.head
        cur_index = 0
        while cur_index < index:
            cur_index += 1
            cur = cur.next
        return cur

    def delete_node(self, prev_node):
        if prev_node.next == self.head:
            self.head = self.head.next
        if prev_node.next == self.tail:
            self.tail = prev_node
        prev_node.next = prev_node.next.next


def josephus_problem(n, k):
    linked_list = LinkedList(1)
    for i in range(2, n+1):
        linked_list.append(i)

    josephus_arr = []
    prev = linked_list.tail
    while n > 0:
        for _ in range(k-1):
            prev = prev.next
        josephus_arr.append(prev.next.data)
        linked_list.delete_node(prev)
        n -= 1
    # 아래 방법은 불필요한 탐색이 증가되어 비효율적이고, 단순히 index로 접근하면 prev_node를 찾기위해
    # 추가적인 탐색이 필요
    # for i in range(1, n+1):
    #     idx = k - 1
    #     # print(linked_list.get_node(idx).data)
    #     josephus_arr.append(linked_list.get_node(idx).data)
    #     # 3번째 링크드리스트 삭제
    #     linked_list.delete_node(idx)
    #     # head 위치 변경
    #     linked_list.head = linked_list.get_node(idx)

    print("<"+", ".join(map(str, josephus_arr))+">")

n, k = map(int, input().split())
josephus_problem(n, k)