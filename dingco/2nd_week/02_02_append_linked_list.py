class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
node = Node(5)
print(node.data, node.next)

next_node = Node(3)
node.next = next_node
class LinkedList:
    def __init__(self, value):
        self.head = Node(value)

    # linkedlist 의 가장 끝에 있는 노드에 새로운 노드를 연결해줘
    def append(self, value):
        cur = self.head
        while cur.next is not None:
            cur = cur.next
        cur.next = Node(value)

    # linkedlist 에서 저장한 head 를 따라가면서 현재 있는 노드들을 전부 출력해주는함수
    def print_all(self):
        cur = self.head
        while cur is not None:
            print(cur.data)
            cur = cur.next


linkedlist = LinkedList(5)
print(linkedlist.head.data)

linkedlist.append(12)
linkedlist.append(8)
linkedlist.print_all()