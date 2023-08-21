# SHOW ME THE DUNGEON
import sys
import heapq


if __name__ == "__main__":
    N, K = map(int, sys.stdin.readline().split())
    monsters = list(map(int, sys.stdin.readline().split()))
    people = list(map(int, sys.stdin.readline().split()))

    island_info = list()
    for i in range(N):
        island_info.append([i, people[i], monsters[i]])

    answer = 0

    island_info.sort(key=lambda x: (-x[1], x[2]))
    # print(island_info)
    cur_cost = 0
    cur_idx = 0
    while True:
        for i in range(cur_idx, len(island_info)):
            if K - (island_info[i][2]+cur_cost) >= 0:
                cur_cost += island_info[i][2]
                K -= cur_cost
                answer += island_info[i][1]
                cur_idx = i+1

        break

    print(answer)
