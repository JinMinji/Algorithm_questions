#Contest339, Q1

class Solution:
    def findTheLongestBalancedSubstring(self, s: str) -> int:
        res = 0
        cur_zero_cnt = 0
        cur_one_cnt = 0
        flag = False
        for i in range(len(s)):
            if flag and s[i] == '1':   # 앞에 1이 나왔고, 현재가 1일 때
                cur_one_cnt += 1
                if cur_one_cnt <= cur_zero_cnt:
                    res = max(res, cur_one_cnt*2)

            elif flag and s[i] == '0':  # 앞에 1이 나왔고, 현재가 0일 때
                cur_zero_cnt = 1
                cur_one_cnt = 0
                flag = False

            elif not flag and s[i] == '1':  # 앞에 1이 나오지 않았고, 현재가 1일 때
                flag = True
                cur_one_cnt = 1
                if cur_one_cnt <= cur_zero_cnt:
                    res = max(res, cur_one_cnt*2)

            elif not flag and s[i] == '0':    # 앞에 1이 나오지 않았고, 현재가 0일 때
                cur_zero_cnt += 1

            # print(i, res, flag, cur_one_cnt, cur_zero_cnt)
        return res


if __name__ == '__main__':
    test = Solution()
    answer = test.findTheLongestBalancedSubstring(s = "01000111")
    print(answer)
    answer = test.findTheLongestBalancedSubstring(s = "00111")
    print(answer)
    answer = test.findTheLongestBalancedSubstring(s = "1011")
    print(answer)