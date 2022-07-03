#숨바꼭질, 골드 5
from collections import deque


if __name__ == "__main__":
    N, K = map(int, input().split())

    time = 10**6
    way_cnt = 0

    to_visit = deque()
    to_visit.append([0, N])

    visited = [10**5 for i in range(10**5+1)]

    while to_visit:
        cur_time, cur_loc = to_visit.popleft()
        if visited[cur_loc] < cur_time:
            continue

        visited[cur_loc] = cur_time

        if cur_time > time:
            break

        if cur_loc == K:
            if cur_time < time:
                way_cnt = 1
                time = cur_time
                continue
            else: # cur_time == time:
                way_cnt += 1
                continue

        if cur_loc + 1 <= 10**5:
            to_visit.append([cur_time + 1, cur_loc + 1])

        if cur_loc - 1 >= 0:
            to_visit.append([cur_time + 1, cur_loc - 1])

        if cur_loc*2 <= 10**5:
            to_visit.append([cur_time + 1, cur_loc*2])


    print(time)
    print(way_cnt)