#Contest343, Q1

from typing import List

class Solution:
    def isWinner(self, player1: List[int], player2: List[int]) -> int:
        double = [2 if player1[0] == 10 else 1, 2 if player2[0] == 10 else 1]
        score = [player1[0], player2[0]]
        for i in range(1, len(player1)):
            score[0] += player1[i] * double[0]
            score[1] += player2[i] * double[1]
            double[0] = 2 if player1[i] == 10 or player1[i-1] == 10 else 1
            double[1] = 2 if player2[i] == 10 or player2[i-1] == 10 else 1

        if score[0] > score[1]:
            return 1
        elif score[0] == score[1]:
            return 0
        else:
            return 2

if __name__ == "__main__":
    test = Solution()
    # print(test.isWinner(player1 = [4,10,7,9], player2 = [6,5,2,3]))
    # print(test.isWinner(player1 = [3,5,7,6], player2 = [8,10,10,2]))
    # print(test.isWinner(player1 = [2,3], player2 = [4,1]))
    print(test.isWinner([10,2,2,3], [3,8,4,5]))


