# Contest368, Q3

from typing import List

class Solution:
    def minGroupsForValidAssignment(self, nums: List[int]) -> int:
        cnt = dict()
        for i in range(len(nums)):
            cnt[nums[i]] = cnt.get(nums[i], 0) + 1
        
        cnts = list(cnt.values())

        cnts.sort()
        
        print(cnt)
        print(cnts)

        max_size = cnts[0] + 1

        for i in range(max_size, 1, -1):
            print(i)
            answer = 0
            for j in range(len(cnts)):
                if cnts[j] % i == 0:
                    answer += cnts[j] // i 
                    print(i, 'case same', cnts[j], answer)
                    continue
                if cnts[j] % i == i-1:
                    answer += (cnts[j] // i + 1)
                    print(i, 'case lower', cnts[j], answer)
                    continue
                
                if cnts[j] % (i-1) == 0:
                    answer += cnts[j] // (i-1) 
                    print(i, 'case same', cnts[j], answer)
                    continue
                if cnts[j] % (i-1) == 1 and cnt[j] > (i-1):
                    answer += cnts[j] // (i-1)
                    print(i, 'case lower', cnts[j], answer)
                    continue

                break
            else:
                print(i, j, answer)
                return answer


if __name__ == "__main__":
    test = Solution()
    # print(test.minGroupsForValidAssignment(nums = [3,2,3,2,3]))
    # print(test.minGroupsForValidAssignment(nums = [10,10,10,3,1,1]))
    # print(test.minGroupsForValidAssignment([1,1,1,3,1,2,2,2,3]))
    print(test.minGroupsForValidAssignment([1,1,3,3,3,3,1,3,1,1,1,2,2,1]))
    # print(test.minGroupsForValidAssignment([2,1,1,2,2,3,1,3,1,1,1,1,2]))