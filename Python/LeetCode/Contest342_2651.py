#Contest342, Q1

class Solution:
    def findDelayedArrivalTime(self, arrivalTime: int, delayedTime: int) -> int:
        return (arrivalTime + delayedTime) % 24


if __name__ == "__main__":
    test = Solution()
    print(test.findDelayedArrivalTime(15, 5))
    print(test.findDelayedArrivalTime(13, 11))


