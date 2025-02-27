class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class Tree:
    def __init__(self, node=None):
        self.root = node
    def levelorder(self):
        res = []
        if not self.root:
            return res
        q = [self.root]
        while q:
            node = q.pop(0)
            res.append(node.data)
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
        return res
    # def make_tree(self, arr): # 배열로 이진트리 만들기.
    #     if not arr:
    #         return
    #     self.root = Node(arr[0])
    #     q = [self.root]
    #     idx = 1
    #     while q:
    #         node = q.pop()
    #         # if

def insert(tree, key):
    node = Node(key)
    if tree.root is None:
        tree.root = node
    else:
        q = [tree.root]
        while q:
            popnode = q.pop(0)
            if popnode.left is None:
                popnode.left = node
                break
            else:
                q.append(popnode.left)
            if popnode.right is None:
                popnode.right = node
                break
            else:
                q.append(popnode.right)


tree = Tree(Node(10))
tree.root.left = Node(11)
tree.root.right = Node(9)
tree.root.left.left = Node(7)
tree.root.right.left = Node(15)
tree.root.right.right = Node(8)
print(tree.levelorder())
insert(tree, 12)
print(tree.levelorder())
# tree = [10, 11, 9, 7, 15, 8]
# insert(tree, 12)
# q = [tree.root]
# print(q)
# res = []
# while q:
#     n = q.pop(0)
#     res.append(n.data)
#     if n.left:
#         q.append(n.left)
#     if n.right:
#         q.append(n.right)
# print(res)
# print(tree.root.data)