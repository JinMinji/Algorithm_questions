# 택배, 골드 3


if __name__ == '__main__':
    N, C = map(int, input().split(' '))

    M = int(input())

    boxes = list()

    for i in range(M):
        a, b, n = map(int, input().split())
        boxes.append([a, b, n])

    boxes.sort(key=lambda x: x[1])  # 받는 마을 순서로 결정

    total = 0
    cur_truck = 0
    truck_boxes = [0 for i in range(N+1)]
    # truck_boxes[n] : n마을에서 들고있는 박스개수
    for i in range(len(boxes)):
        cur_truck +=



