# Contest346, Q4

from typing import List

class Solution:
    def modifiedGraphEdges(self, n: int, edges: List[List[int]], source: int, destination: int, target: int) -> List[List[int]]:

        return


if __name__ == "__main__":
    test = Solution()
    print(test.modifiedGraphEdges(n = 5, edges = [[4,1,-1],[2,0,-1],[0,3,-1],[4,3,-1]], source = 0, destination = 1, target = 5))
    print(test.modifiedGraphEdges(n = 3, edges = [[0,1,-1],[0,2,5]], source = 0, destination = 2, target = 6))
    print(test.modifiedGraphEdges(n = 4, edges = [[1,0,4],[1,2,3],[2,3,5],[0,3,-1]], source = 0, destination = 2, target = 6))