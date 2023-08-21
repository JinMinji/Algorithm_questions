#Contest343, Q3

from typing import List

class Solution:
    def minimumCost(self, start: List[int], target: List[int], specialRoads: List[List[int]]) -> int:
        INF = 10**6
        max_x = max(start[0], target[0])
        max_y = max(start[1], target[1])
        costs = [[INF for i in range(max_y+1)] for i in range(max_x+1)]

        for i in range(max_x + 1):
            for j in range(max_y + 1):
                costs[i][j] = abs(start[0] - i) + abs(start[1] - j)

        # 다익스트라, start -> end, start -> 스페셜 출발지점, 스페셜 도착지점 -> end, 스페셜 도착지점 -> 스페셜 출발지점
        for road in specialRoads:
            i, j, x, y, c = road
            costs[x][y] = min(costs[x][y], costs[i][j] + c)

        for i in range(len(costs)):
            print(costs[i])

        return costs[target[0]][target[1]]


if __name__ == "__main__":
    test = Solution()
    print(test.minimumCost(start = [1,1], target = [4,5], specialRoads = [[1,2,3,3,2],[3,4,4,5,1]]))
    print(test.minimumCost(start = [3,2], target = [5,7], specialRoads = [[3,2,3,4,4],[3,3,5,5,5],[3,4,5,6,6]]))
    # print(test.minimumCost())
    # print(test.minimumCost())


