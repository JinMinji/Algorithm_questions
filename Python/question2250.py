# 트리의 높이와 너비

node_num = int(input())

class Node:
    def __init__(self, data, left, right):
        self.parent = -1 # 루트노드가 뭔지 알 수 없으니, 루트일 경우 parent값을 -1로 설정하여 루트를 확인할 수 있도록 한다.
        self.level = 1
        self.data = data
        self.left = left
        self.right = right
    level = parent.level + 1

def in_order(node):
    if node.left != -1:
        in_order(tree[node.left])
    in_order_lst.append(node.data)
    if node.right != -1:
        in_order(tree[node.right])
    return in_order_lst

def bfs(tree, start):
    visited = list()
    need_visit = list()

    need_visit.append(start)
    while need_visit:
        node = need_visit.pop(0)
        if node not in visited:
            visited.append(node)
            need_visit.extend(tree[node])  # extend!!

    return visited

tree = dict()
for i in range(node_num):
    d, l, r = map(int, input().split())

    tree[d] = Node(d,l,r)

in_order_lst = []
in_order(tree[1])
print(in_order_lst)


