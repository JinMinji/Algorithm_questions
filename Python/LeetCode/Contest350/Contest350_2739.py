# Contest350, Q1

class Solution:
    def distanceTraveled(self, mainTank: int, additionalTank: int) -> int:
        result = 0
        while mainTank >= 5 and additionalTank > 0:
            result += 10*5
            mainTank -= 5
            additionalTank -= 1
            mainTank += 1
        result += 10*mainTank
        return result

if __name__ == "__main__":
    test = Solution()
    print(test.distanceTraveled(mainTank = 5, additionalTank = 10))
    print(test.distanceTraveled(mainTank = 1, additionalTank = 2))
    # print(test.minCost())
