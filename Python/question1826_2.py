#연료채우기, 골드3
#최대힙 써서 푸는 방법, 맞았습니다.

import heapq


if __name__ == "__main__":
    N = int(input())
    gas_station = list()
    for i in range(N):
        idx, oil = map(int, input().split())
        gas_station.append([idx, oil])

    gas_station.sort(key=lambda x: x[0])
    distance, cur_oil = map(int, input().split())

    answer = 0
    can_go = 0
    can_go += cur_oil
    oil_heap = list()

    while can_go < distance:     #현재 위치 + 가진 오일이 목적지를 넘기 전까지만 확인
        answer += 1
        while gas_station:
            if gas_station[0][0] <= can_go:
                tmp = gas_station.pop(0)
                heapq.heappush(oil_heap, (-tmp[1], tmp[1]))
                # print(can_go, "now : ", oil_heap)
            else:
                break

        if not oil_heap:
            answer = -1
            break

        tmp_oil = heapq.heappop(oil_heap)
        # print("oil_list", oil_heap)
        # print("pop :", tmp_oil[1])
        can_go += tmp_oil[1]

    print(answer)

