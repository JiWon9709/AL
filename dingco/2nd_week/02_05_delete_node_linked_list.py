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

    def print_all(self):
        cur = self.head
        while cur is not None:
            print(cur.data)
            cur = cur.next

    def get_node(self, index):
        node = self.head
        count = 0
        while count < index:
            node = node.next
            count += 1
        return node

    def add_node(self, index, value):
        new_node = Node(value)
        if index == 0:
            new_node.next = self.head
            self.head = new_node
            return

        node = self.get_node(index - 1)
        next_node = node.next
        node.next = new_node
        new_node.next = next_node

    def delete_node(self, index):
        target_node = self.get_node(index)
        # 5 -> 12 -> 3
        # 12 -> 3
        # 0번째 인덱스일때
        if index == 0:
            self.head = target_node.next
            target_node.next = None
            return
        # 5->12->3
        # 5->3
        prev_node = self.get_node(index-1)
        prev_node.next = target_node.next
        target_node.next = None

        return "index 번째 Node를 제거해주세요!"


linked_list = LinkedList(5)
linked_list.append(12)
linked_list.append(3)
linked_list.delete_node(2)
linked_list.print_all()