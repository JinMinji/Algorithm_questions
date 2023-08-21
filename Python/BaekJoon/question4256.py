# 트리

def postorder(v):
    global tree
    if tree[v][0] != 0:
        postorder(tree[v][0])
    if tree[v][1] != 0:
        postorder(tree[v][1])
    print(v, end=' ')


def make_tree(sub_inorder_list):
    global tree, cur_idx, pre_order
    print(pre_order[cur_idx])
    if pre_order[cur_idx] in sub_inorder_list:
        mid_idx = sub_inorder_list.index(pre_order[cur_idx])

    else:
        return

    if mid_idx != 0:
        left_list = sub_inorder_list[:mid_idx]
        print('left', left_list)
        if cur_idx < len(pre_order) and pre_order[cur_idx+1] in left_list:
            tree[pre_order[cur_idx]][0] = pre_order[cur_idx+1]
        if len(left_list) == 1:
            print(pre_order[cur_idx])
            tree[pre_order[cur_idx]][0] = left_list[0]
            cur_idx += 1

        else:
            cur_idx += 1
            make_tree(left_list)
        
    if mid_idx + 1 < len(sub_inorder_list):
        right_list = sub_inorder_list[mid_idx + 1:]
        print('right', right_list)
        if cur_idx < len(pre_order) and pre_order[cur_idx+1] in right_list:
            tree[pre_order[cur_idx]][1] = pre_order[cur_idx+1]
        
        if len(right_list) == 1:
            tree[pre_order[cur_idx]][1] = right_list[0]
            cur_idx += 1
        else:
            cur_idx += 1
            make_tree(right_list)
        
        
if __name__ == '__main__':
    T = int(input())

    for t in range(T):
        n = int(input())
        pre_order = list(map(int, input().split()))
        in_order = list(map(int, input().split()))

        tree = [[0, 0] for i in range(n+1)]

        root = pre_order[0]
        cur_idx = 0

        make_tree(in_order)
        for t in range(len(tree)):
            print(t, 'left :', tree[t][0], 'right :', tree[t][1])

        postorder(pre_order[0])     # root는 preorder[0]
