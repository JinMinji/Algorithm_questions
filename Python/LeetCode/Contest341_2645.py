#Contest341, Q3

class Solution:
    def addMinimum(self, word: str) -> int:
        valid_str = ['a', 'b', 'c']
        before = 2
        ans_cnt = 0
        for s in word:
            if s == valid_str[(before+1)%3]:
                before = (before+1)%3
                continue
            elif s == valid_str[(before+2)%3]:
                ans_cnt += 1
                before = (before+2)%3
            elif s == valid_str[(before)%3]:
                ans_cnt += 2

        if word[-1] == 'c':
            return ans_cnt
        elif word[-1] == 'b':
            return ans_cnt + 1
        else:
            return ans_cnt + 2


if __name__ == "__main__":
    test = Solution()
    print(test.addMinimum('b'))
    print(test.addMinimum('aaa'))
    print(test.addMinimum('abc'))


