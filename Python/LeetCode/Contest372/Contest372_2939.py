# Contest372, Q3

from typing import List

class Solution:
    def maximumXorProduct(self, a: int, b: int, n: int) -> int:
        answer = 0
        for i in range(2**n):
            answer = max(answer, (a^i) * (b^i)) 
        return answer % (10**9 + 7)
        
if __name__ == "__main__":
    test = Solution()
    print(test.maximumXorProduct(a = 12, b = 5, n = 4))
    print(test.maximumXorProduct(a = 6, b = 7 , n = 5))
    print(test.maximumXorProduct(a = 1, b = 6, n = 3))
