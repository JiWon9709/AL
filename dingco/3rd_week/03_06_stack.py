class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# head 가 last
# LIFO
class Stack:
    def __init__(self):
        self.head = None

    def push(self, value):
        node = Node(value)
        node.next = self.head
        self.head = node

    # pop 기능 구현
    def pop(self):
        if self.is_empty():
            return -1
        delete_head = self.head
        self.head = self.head.next
        return delete_head

    def peek(self):
        if self.is_empty():
            return -1
        return self.head

    # isEmpty 기능 구현
    def is_empty(self):
        return self.head is None

stack = Stack()
stack.push(4)
print(stack.head.data)
stack.push(3)
print(stack.peek().data)
stack.push(5)
print(stack.peek().data)
stack.pop()