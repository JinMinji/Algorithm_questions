# Contest346, Q3

class Solution:
    def findNumber(self, target, cur):
        if not cur or not int(cur):
            if target == 0:
                return True
            else:
                return False
        # print('길이', min(len(str(target)), len(cur))+1)
        for k in range(1, min(len(str(target)), len(cur))+1):    # i의 자릿수가 k면, k길이 이하로만 잘라야함.
            # print(target, k, cur[:k], cur[k:])
            if self.findNumber(target - int(cur[:k]), cur[k:]):
                return True
        return False

    def punishmentNumber(self, n: int) -> int:
        answer = 0
        for i in range(1, n+1):
            # 1000*1000 = 1000000. 즉..!해봐야 7자리고 7자리 나누는 조합이어봐야..?
            # 1*7, 1*5 + 2, 1*3 + 2*2, 1*1 + 2*3, 1*4 + 3*1, 1*2 + 2*1 + 3*1, ... 암튼 몇개 안됨
            if self.findNumber(i, str(i*i)):
                answer += i*i
        return answer


if __name__ == "__main__":
    test = Solution()
    print(test.punishmentNumber(n = 10))
    print(test.punishmentNumber(n = 37))