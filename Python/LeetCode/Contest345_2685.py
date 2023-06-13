# Contest345, Q4

from typing import List
from collections import defaultdict


class Solution:
    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:
        edges_dict = defaultdict(list)
        answer = 0
        for i in range(len(edges)):
            a, b = edges[i]
            edges_dict[a].append(b)
            edges_dict[b].append(a)

        graph_num = [0 for i in range(n)]
        graph_cnt = 0
        for i in range(n):
            if graph_num[i] != 0:
                continue
            graph_cnt += 1
            to_visit = [i]
            graph = [i]
            graph_num[i] = graph_cnt
            while to_visit:
                v = to_visit.pop(0)
                for adj in edges_dict[v]:
                    if graph_num[adj] == 0:
                        graph_num[adj] = graph_cnt
                        to_visit.append(adj)
                        graph.append(adj)

            graph.sort()
            flag = True
            for i in range(len(graph)):
                edges_dict[graph[i]].append(graph[i])
                edges_dict[graph[i]].sort()
                if edges_dict[graph[i]] != graph:
                    flag = False
                    break
            if flag:
                answer += 1

        return answer


if __name__ == "__main__":
    test = Solution()
    print(test.countCompleteComponents(n = 6, edges = [[0,1],[0,2],[1,2],[3,4]]))
    print(test.countCompleteComponents(n = 6, edges = [[0,1],[0,2],[1,2],[3,4],[3,5]]))