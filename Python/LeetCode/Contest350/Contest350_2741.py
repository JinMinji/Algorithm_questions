# Contest350, Q3

from typing import List
from collections import defaultdict, deque


class Solution:
    def specialPerm(self, nums: List[int]) -> int:
        # 인접한 요소끼리 약수/배수 관계.
        can_be = defaultdict(list)
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] % nums[j] == 0 or nums[j] % nums[i] == 0:
                    can_be[nums[i]].append(nums[j])
                    can_be[nums[j]].append(nums[i])
        answer = 0
        can_be[0] = nums
        # print(can_be)
        to_visit = deque()
        to_visit.append((0, []))
        while to_visit:
            cur, visited = to_visit.popleft()
            print(cur, visited)
            for next_num in can_be[cur]:
                if next_num not in visited:
                    if len(visited) == len(nums) - 1:
                        answer += 1
                    elif (next_num, visited) not in to_visit:
                        to_visit.append((next_num, visited + [next_num]))

        return answer


if __name__ == "__main__":
    test = Solution()
    # print(test.specialPerm(nums = [2,3,6]))
    # print(test.specialPerm(nums = [1,4,3]))
    print(test.specialPerm([1,7,28,4,8,16,96,32,64]))
