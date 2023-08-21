# 트리 - 맞았습니다!

def postorder(v):
    global tree, result
    if tree[v][0] != 0:
        postorder(tree[v][0])
    if tree[v][1] != 0:
        postorder(tree[v][1])
    result.append(str(v))


def make_tree(sub_inorder_list, sub_pre_order):
    tmp_root = sub_pre_order[0]
    tmp_mid = sub_inorder_list.index(tmp_root)
    if tmp_mid > 0:
        left_tree = sub_inorder_list[:tmp_mid]
        tree[tmp_root][0] = sub_pre_order[1]
        make_tree(left_tree, sub_pre_order[1:1+len(left_tree)])

    if tmp_mid < len(sub_inorder_list) - 1:
        right_tree = sub_inorder_list[tmp_mid + 1:]
        tree[tmp_root][1] = sub_pre_order[tmp_mid+1]
        make_tree(right_tree, sub_pre_order[tmp_mid+1:])


if __name__ == '__main__':
    T = int(input())
    for t in range(T):
        n = int(input())
        pre_order = list(map(int, input().split()))
        in_order = list(map(int, input().split()))

        tree = [[0, 0] for i in range(n + 1)]

        root = pre_order[0]
        cur_idx = 0

        make_tree(in_order, pre_order)
        # for t in range(len(tree)):
        #     print(t, 'left :', tree[t][0], 'right :', tree[t][1])
        result = list()
        postorder(pre_order[0])  # root는 preorder[0]
        print(' '.join(result))
