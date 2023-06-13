# Contest346, Q1

class Solution:
    def minLength(self, s: str) -> int:
        flg = True
        while len(s) >= 2 and flg:
            for i in range(len(s)):
                if i == len(s)-1:
                    flg = False
                if s[i:i+2] == 'AB' or s[i:i+2] == 'CD':
                    if i == 0:
                        s = s[i+2:]
                    else:
                        s = s[:i] + s[i+2:]
                    break

        return len(s)


if __name__ == "__main__":
    test = Solution()
    print(test.minLength(s = "ABFCACDB"))
    print(test.minLength(s = "ACBBD"))