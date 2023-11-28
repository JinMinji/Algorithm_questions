# Contest370, Q2

from typing import List

class Solution:
    def findChampion(self, n: int, edges: List[List[int]]) -> int:
        dict_winner = [[] for i in range(n)]

        for i in range(len(edges)):
            dict_winner[edges[i][1]].append(edges[i][0])
        
        winner = -1
        for i in range(n):
            if len(dict_winner[i]) == 0:
                if winner != -1:
                    winner = -1
                    break
                winner = i
        return winner

    
if __name__ == "__main__":
    test = Solution()
    print(test.findChampion(n = 3, edges = [[0,1],[1,2]]))
    print(test.findChampion(n = 4, edges = [[0,2],[1,3],[1,2]]))
    # print(test.findChampion([[0,1],[1,2]]))
