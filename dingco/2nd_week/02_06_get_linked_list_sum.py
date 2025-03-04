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

def get_single_linked_list(linked_list_1):
    sum = 0
    cur = linked_list_1.head
    while cur is not None:
        sum = sum * 10 + cur.data
        cur = cur.next
    return sum

# 유지보수성 높이기 위해 get_single_linked_list 함수 생성
def get_linked_list_sum(linked_list_1, linked_list_2):
    sum1 = get_single_linked_list(linked_list_1)
    sum2 = get_single_linked_list(linked_list_2)
    # 똑같은 코드가 반복되면 이상함을 느껴야함!!
    # cur = linked_list_1.head
    # while cur is not None:
    #     # str1 += str(cur.data)
    #     sum1 = sum1 * 10 + cur.data
    #     cur = cur.next
    # cur = linked_list_2.head
    # while cur is not None:
    #     # str2 += str(cur.data)
    #     sum2 = sum2 * 10 + cur.data
    #     cur = cur.next
    # print(str1, str2)
    # return int(str1) + int(str2)
    return sum1 + sum2

linked_list_1 = LinkedList(6)
linked_list_1.append(7)
linked_list_1.append(8)

linked_list_2 = LinkedList(3)
linked_list_2.append(5)
linked_list_2.append(4)

print(get_linked_list_sum(linked_list_1, linked_list_2))