#13913, 숨바꼭질 4, 골드4
from collections import deque


if __name__ == "__main__":
    N, K = map(int, input().split())

    res_time = 10 ** 6  # 최댓값으로 초기화, 1씩 가더래도 10**5이 max!
    ways = []       # 최단 시간으로 잡았을 때, 경로를 담아줄 list
    to_visit = deque()  # 방문할 지점을 담을 리스트, deque을 사용한다
    INF = float('inf')
    to_visit.append([0, N, INF])     # 좌표 위에서의 시간, 수빈이의 위치 담기

    visited = [[10 ** 5, -1] for i in range(10 ** 5 + 1)]
    # 방문체크를 위한 리스트. max로 초기화

    while to_visit:
        cur_time, cur_loc, pre = to_visit.popleft()
        if visited[cur_loc][0] < cur_time:
            continue    # 더 빠른 시간으로 이미 방문했으면, 또 탐색하지 않아도 된다.

        # 담긴 시간보다 더 빠른 시간에 방문했으면, 갱신해준후, 다시 탐색해준다.
        visited[cur_loc] = [cur_time, pre]

        if cur_time > res_time:     # 결과 시간보다 더 작으면, 더 찾을 필요도 없음
            break

        if cur_loc == K:
            if cur_time < res_time:
                res_time = cur_time
                continue
            else:  # cur_time == time:
                continue

        if cur_loc + 1 <= 10 ** 5:
            to_visit.append([cur_time + 1, cur_loc + 1, cur_loc])

        if cur_loc - 1 >= 0:
            to_visit.append([cur_time + 1, cur_loc - 1, cur_loc])

        if cur_loc * 2 <= 10 ** 5:
            to_visit.append([cur_time + 1, cur_loc * 2, cur_loc])


    print(res_time)

    cur = K
    while cur != INF:
        ways.append(cur)
        cur = visited[cur][1]

    print(*ways[::-1])