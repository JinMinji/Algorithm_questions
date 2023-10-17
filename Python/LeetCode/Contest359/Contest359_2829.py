# Contest359, Q2

class Solution:
    def minimumSum(self, n: int, k: int) -> int:
        answer = [i for i in range(1, n+1)]
        cur_max = n
        for i in range(n):
            if 0 < k - answer[i] < answer[i]:
                print(k - answer[i], i, "//", answer[i], k)
                answer[i] = max(cur_max+1, k)
                cur_max = answer[i]
        print(answer)
        return sum(answer)


if __name__ == "__main__":
    test = Solution()
    print(test.minimumSum(n = 5, k = 4))
    print(test.minimumSum(n = 2, k = 6))
    print(test.minimumSum(n = 2, k = 3))