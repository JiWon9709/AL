class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
# head tail
# [4] [3]
# head    tail
# [4] [3] [2]
class Queue:
    def __init__(self):
        self.head = None
        self.tail = None

    def enqueue(self, value):
        new_node = Node(value)
        if self.is_empty():
            self.head = new_node
            self.tail = new_node
            return
        self.tail.next = new_node
        self.tail = new_node

    def dequeue(self):
        if self.is_empty():
            return "queue is empty"
        delete_head = self.head
        self.head = self.head.next
        return delete_head

    def peek(self):
        # 맨앞 값만 표시
        if self.is_empty():
            return "queue is empty"
        return self.head.data

    def is_empty(self):
        return self.head is None

queue = Queue()
queue.enqueue(4)
print(queue.peek())
queue.enqueue(3)
print(queue.peek())
queue.enqueue(2)
print(queue.peek())
queue.dequeue()
print(queue.peek())