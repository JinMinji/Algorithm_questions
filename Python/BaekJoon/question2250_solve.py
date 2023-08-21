class Node:
    def __init__(self, number, left, right):
        self.parent  = -1 #head는 parent가 -1 이다.
        self.number = number
        self.left = left
        self.right = right


def in_order(node, level): # 중위순회를 사용하여 푼다.
    global level_depth, x
    level_depth = max(level_depth, level)
    if node.left != -1: # 왼쪽 노드가 있으면
        in_order(tree[node.left], level+1)
    level_min[level] = min(level_min[level], x)
    level_max[level] = max(level_max[level], x)
    x += 1 # x좌표 맨~왼쪽에 있는 것부터 1
    if node.right != -1:
        in_order(tree[node.right], level+1)

n = int(input())
tree = dict()

level_min = [n] #레벨이 1부터시작해서, 0번째에는 그냥 임의의 값을 담아둔다.
level_max = [0]

root = -1 # root의 parent는 -1
x = 1
level_depth = 1

for i in range(1, n+1):
    tree[i] = Node(i, -1, -1) #Default로 노드들 미리 생성 (부모-자식연결을 위해)
    level_min.append(n)
    level_max.append(0)

for i in range(n):
    number, left, right = map(int, input().split())
    tree[number].left = left
    tree[number].right = right
    if left != -1:
        tree[left].parent = number
    if right != -1:
        tree[right].parent = number

for i in range(1, n+1):
    if tree[i].parent == -1 # root찾기
        root = i

in_order(tree[root], 1)

result_level = 1
result_width = level_max[1]-level_min[1]+1
for i in range(2, level_depth+1):
    width = level_max[i]-level_min[i]+1
    if result_width < width:
        result_level = i
        result_width = width

print(result_level, result_width)