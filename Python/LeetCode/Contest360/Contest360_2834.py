# Contest360, Q2

class Solution:
    def minimumPossibleSum(self, n: int, target: int) -> int:
        h_target = target//2
        if h_target >= n:
            return (n*(n+1)//2) % (10**9+7)
        else:
            return (h_target*(h_target+1)//2 + (target+target+n-h_target-1)*(n-h_target)//2) % (10**9+7)


if __name__ == "__main__":
    test = Solution()
    print(test.minimumPossibleSum(n=2, target=3))
    print(test.minimumPossibleSum(n=3, target=3))
    print(test.minimumPossibleSum(n=1, target=1))

