# Contest352, Q2

from typing import List


class Solution:
    def make_prime_list(self, n):
        prime_list = [-1 for i in range(n + 1)]
        for i in range(n):
            if i == 2 or i == 3:
                prime_list[i] = True
                continue

            if i % 2 == 0 or i < 2:
                prime_list[i] = False
                continue

            for j in range(3, int(i ** 0.5) + 1, 2):
                if i % j == 0:
                    prime_list[i] = False
                    break

            if prime_list[i] == -1:
                prime_list[i] = True

        return prime_list

    def findPrimePairs(self, n: int) -> List[List[int]]:
        answer = []
        prime_list = self.make_prime_list(n)
        for i in range(1, n // 2 + 1):
            if prime_list[i] and prime_list[n-i]:
                answer.append([i, n-i])

        return answer


if __name__ == "__main__":
    test = Solution()
    print(test.findPrimePairs(n = 10))
    print(test.findPrimePairs(n = 2))
    print(test.findPrimePairs(n = 999999))
