# Contest 334, Q4

from typing import List
import heapq

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def minimumTime(grid: List[List[int]]) -> int:
    to_visit = []
    if grid[0][1] <= 1:
        heapq.heappush(to_visit, [1, 0, 1])
    if grid[1][0] <= 1:
        heapq.heappush(to_visit, [1, 1, 0])

    target_loc = [len(grid)-1, len(grid[0])-1]
    visited = [[0 for i in range(len(grid[0]))] for i in range(len(grid))]
    while to_visit:
        cur_info = heapq.heappop(to_visit)
        # print(cur_info, grid[cur_info[1]][cur_info[2]])
        # print(to_visit)
        if [cur_info[1], cur_info[2]] == target_loc:
            return cur_info[0]

        for i in range(4):
            x = cur_info[1] + dx[i]
            y = cur_info[2] + dy[i]
            if 0 <= x < len(grid) and 0 <= y < len(grid[0]) and visited[x][y] == 0:
                visited[x][y] = 1
                if cur_info[0] + 1 >= grid[x][y]:
                    heapq.heappush(to_visit, [cur_info[0]+1, x, y])
                    print(cur_info, '->', [cur_info[0]+1, x, y])
                else:
                    time_gap = grid[x][y] - cur_info[0]
                    if time_gap % 2 == 0:
                        heapq.heappush(to_visit, [grid[x][y] + 1, x, y])
                        print(cur_info, '->', [grid[x][y] + 1, x, y])
                    else:
                        heapq.heappush(to_visit, [grid[x][y], x, y])
                        print(cur_info, '->', [grid[x][y], x, y])

    return -1


if __name__ == '__main__':
    grid = [[0,1,3,2],[5,1,2,5],[4,3,8,6]]
    answer = minimumTime(grid)
    print('case1:', answer)

    grid = [[0,2,4],[3,2,1],[1,0,4]]
    answer = minimumTime(grid)
    print('case2:', answer)

    grid = [[0,1,99],[3,99,99],[4,5,6]]
    answer = minimumTime(grid)
    print('case3:', answer)


[[0,1,99],
 [3,99,99],
 [4,5,6]]