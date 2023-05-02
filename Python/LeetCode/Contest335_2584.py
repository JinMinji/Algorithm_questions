#Contest335, Q4

from typing import List
from queue import Queue

class Solution:
    def factorization(self, x):
        cnt_arr = []
        div_num = 2
        while div_num <= x:
            if x % div_num == 0:
                cnt_arr.append(div_num)
                x = x / div_num
            else:
                div_num = div_num + 1
        cnt_arr = list(set(cnt_arr))

        return cnt_arr

    def gcd(self, x, y):  # greatest common divisor
        while y != 0:
            r = x % y
            x = y
            y = r

        return x

    def findValidSplit(self, nums: List[int]) -> int:
        print(nums)
        left = Queue()
        right = Queue()
        prime_nums = []
        for i in range(len(nums)):
            cur_cnt = self.factorization(nums[i])
            prime_nums.append(cur_cnt)
            for n in cur_cnt:
                right.put(n)
            print(i, nums[i], prime_nums[i])
        print(prime_nums)

        answer = -1
        for i in range(len(nums)-2):
            for n in prime_nums[i]:
                right.get()
                left.put(n)

            tmp = list(set(right.queue))
            tmp.extend(list(set(left.queue)))

            set_tmp = list(set(tmp))
            if len(tmp) == len(set_tmp):
                answer = i

        return answer


if __name__ == '__main__':
    test1 = Solution()
    answer = test1.findValidSplit([4,7,15,8,3,5])
    print(answer)
    answer = test1.findValidSplit([4,7,8,15,3,5])
    print(answer)
    answer = test1.findValidSplit([557663,280817,472963,156253,273349,884803,756869,763183,557663,964357,821411,887849,891133,453379,464279,574373,852749,15031,156253,360169,526159,410203,6101,954851,860599,802573,971693,279173,134243,187367,896953,665011,277747,439441,225683,555143,496303,290317,652033,713311,230107,770047,308323,319607,772907,627217,119311,922463,119311,641131,922463,404773,728417,948281,612373,857707,990589,12739,9127,857963,53113,956003,363397,768613,47981,466027,981569,41597,87149,55021,600883,111953,119083,471871,125641,922463,562577,269069,806999,981073,857707,831587,149351,996461,432457,10903,921091,119083,72671,843289,567323,317003,802129,612373])
    print(answer)