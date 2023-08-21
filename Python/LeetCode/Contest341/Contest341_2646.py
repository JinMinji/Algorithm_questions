#Contest341, Q4

from typing import List
from collections import defaultdict

class Solution:
    def minimumTotalPrice(self, n: int, edges: List[List[int]], price: List[int], trips: List[List[int]]) -> int:
        answer = 0
        edge_dict = defaultdict(list)
        for i in range(len(edges)):
            edge_dict[edges[i][0]].append([edges[i][1], price[i]])
            edge_dict[edges[i][1]].append([edges[i][0], price[i]])

        for i in range(len(trips)):
            cost = 0
            cur = trips[i][0]



if __name__ == "__main__":
    test = Solution()
    print(test.minimumTotalPrice())
    print(test.minimumTotalPrice())


