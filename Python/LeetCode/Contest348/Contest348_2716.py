# Contest348, Q1

class Solution:
    def minimizedStringLength(self, s: str) -> int:
        check_alpha = [0 for i in range(26)]
        for c in s:
            check_alpha[ord(c) - 97] = 1

        return sum(check_alpha)


if __name__ == "__main__":
    test = Solution()
    print(test.minimizedStringLength(s = "aaabc"))
    print(test.minimizedStringLength(s = "cbbd"))
    print(test.minimizedStringLength(s = "dddaaa"))