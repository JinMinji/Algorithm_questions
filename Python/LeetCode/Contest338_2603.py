#Contest338, Q4

from typing import List

class Solution:
    def collectTheCoins(self, coins: List[int], edges: List[List[int]]) -> int:
        MAX = len(coins)
        distances = [[MAX for i in range(len(coins))] for i in range(len(coins))]
        edges_dict = {}
        for i in range(len(edges)):
            a, b = edges[i]
            distances[a][b] = 1
            distances[b][a] = 1
            edges_dict[a] = edges_dict.get(a, []).append(b)
            edges_dict[b] = edges_dict.get(b, []).append(a)

        for i in range(len(coins)):
            if not coins[i]:
                continue
            result = [-1 for i in range(len(coins))]
            result[i] = 0
            to_visit = [(i, 0)]
            while to_visit:
                x, d = to_visit.pop()
                for y in edges_dict[x].items():
                    if result[y] == -1:
                        result[y] = d+1
                        to_visit.append((y, d+1))
            distances[i] = result

        sum_dis = [-1 for i in range(len(coins))]
        for i in range(len(coins)):
            cur_sum = 0
            if coins[i]:
                for j in range(len(coins)):
                    cur_sum += coins[i][j]
            sum_dis[i] = []

        return distances


if __name__ == '__main__':
    test = Solution()
    answer = test.collectTheCoins(coins = [1,0,0,0,0,1],
                                  edges = [[0,1],[1,2],[2,3],[3,4],[4,5]])
    print(answer)
    answer = test.collectTheCoins(coins = [0,0,0,1,1,0,0,1],
                                  edges = [[0,1],[0,2],[1,3],[1,4],[2,5],[5,6],[5,7]])
    print(answer)