#Contest335, Q1

class Solution:
    def passThePillow(self, n: int, time: int) -> int:
        if n > time:
            return time + 1
        # n명 일 때, 1번째 사람에서 다시 한바퀴돌아 1번째 사람으로 돌아오기 위한 time은
        # (n-1)*2
        cnt = time % ((n-1)*2)
        print(n, cnt)
        if cnt > (n-1):
            return n - (cnt - (n-1))
        else:
            return cnt + 1


if __name__ == '__main__':
    test = Solution()
    answer = test.passThePillow(4, 5)
    print(answer)
    answer = test.passThePillow(3, 2)
    print(answer)
    answer = test.passThePillow(9, 4)
    print(answer)
    answer = test.passThePillow(18, 38)
    print(answer)
    #
    #
    # 0 1 2 3 4 5 6 7 8 9 10 11 12
    # 1 2 3 4 3 2 1 2 3 4 3  2  1

