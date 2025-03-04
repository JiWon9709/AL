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
        node = Node(value)
        # 0 일때는 어떻게 해야할까?
        # head 를 새로 지정
        if index == 0:
            next_node = self.head
            self.head = node
            # return
        else:
            before_node = self.get_node(index-1)
            next_node = before_node.next
            before_node.next = node

        node.next = next_node
        # return "index 번째 Node 뒤에 value 를 추가하세요!"


linked_list = LinkedList(5)
linked_list.append(12)
linked_list.add_node(2, 3)
linked_list.print_all()