#숨바꼭질, 골드 5 -> heapq
import heapq


if __name__ == "__main__":
    N, K = map(int, input().split())

    time = 10**6
    way_cnt = 0

    to_visit = [(0, N)]

    while to_visit:
        cur_time, cur_loc = heapq.heappop(to_visit)

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
            heapq.heappush(to_visit, (cur_time + 1, cur_loc + 1))

        if cur_loc - 1 >= 0:
            heapq.heappush(to_visit, (cur_time + 1, cur_loc - 1))

        if cur_loc*2 <= 10**5:
            heapq.heappush(to_visit, (cur_time + 1, cur_loc * 2))

    print(time)
    print(way_cnt)