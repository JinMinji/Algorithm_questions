from collections import deque


def shift_row(arr):
    tmp = arr.pop()
    arr.appendleft(tmp)
    print(arr)
    # for i in range(len(arr)-1):
    #     res.append(arr[i])

    return arr


def rotate(arr):
    cur = arr[0][0]

    # →
    for j in range(1, len(arr[0])):
        arr[0][j], cur = cur, arr[0][j]
    # ↓
    for i in range(1, len(arr)):
        arr[i][-1], cur = cur, arr[i][-1]
    # ←
    for j in range(2, len(arr[0]) + 1):
        arr[-1][-j], cur = cur, arr[-1][-j]
    # ↑
    for i in range(len(arr) - 2, -1, -1):
        arr[i][0], cur = cur, arr[i][0]

    return arr


def solution(rc, operations):
    answer = [[]]

    rc = deque(rc)

    for op in operations:
        if op == "Rotate":
            rc = rotate(rc)
        else:
            rc = shift_row(rc)

    return rc


if __name__ == "__main__":
    tmp = solution([[1, 2, 3], [4, 5, 6], [7, 8, 9]], ["Rotate", "ShiftRow"])
    # tmp = solution([[1, 2, 3], [4, 5, 6], [7, 8, 9]], ["Rotate"])
    for i in range(len(tmp)):
        print(tmp[i])