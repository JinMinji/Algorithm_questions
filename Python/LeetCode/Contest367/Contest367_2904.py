# Contest367, Q2

from typing import List

class Solution:
    def shortestBeautifulSubstring(self, s: str, k: int) -> str:
        answer = ""
        min_len = len(s)
        cnt = 0
        one_idx = []
        if s[0] == '1':
            cnt = 1
            one_idx.append(0)
        if k == cnt:
            return "1"
        for i in range(1, len(s)):
            if s[i] == '1':
                cnt += 1
                one_idx.append(i)
                if cnt > k:
                    one_idx.pop(0)
                    cnt -= 1
                if cnt == k:
                    if min_len-1 > i - one_idx[0]:
                        answer = s[one_idx[0]:i+1]
                        min_len = len(answer)
                        # print(i, one_idx, one_idx[0], answer, min_len, i - one_idx[0])
                        # print(i, "cur_answer : ", answer)
                    if min_len-1 == i - one_idx[0]:
                        # print(answer, int(answer, 2), s[one_idx[0]:i+1], int(s[one_idx[0]:i+1], 2))
                        if answer == "" or int(answer, 2) > int(s[one_idx[0]:i+1], 2):
                            answer = s[one_idx[0]:i+1]
                        # print(i, one_idx, one_idx[0], answer)
                        # print(i, "cur_answer : ", answer)
        return answer
        
if __name__ == "__main__":
    test = Solution()
    # print(test.shortestBeautifulSubstring(s = "100011001", k = 3))
    # print(test.shortestBeautifulSubstring(s = "1011", k = 2))
    # print(test.shortestBeautifulSubstring(s = "000", k = 1))
    # print(test.shortestBeautifulSubstring(s ="01011101000111110", k = 5))
    print(test.shortestBeautifulSubstring("1111111011111", 12))
    # print(test.shortestBeautifulSubstring(s="1100100101011001001", k=7))
    # print(test.shortestBeautifulSubstring(s="110101000010110101", k=3))
