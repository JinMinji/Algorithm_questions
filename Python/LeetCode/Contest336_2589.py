#Contest336, Q4

from typing import List

class Solution:
    def findMinimumTime(self, tasks: List[List[int]]) -> int:
        tasks.sort(key=lambda x: (x[1], x[0]))
        using_time = [0 for i in range(tasks[-1][1]+1)]

        for i in range(len(tasks)):
            start, end, duration = tasks[i]
            for t in range(start, end+1):
                if using_time[t]:
                    duration -= 1

            for t in range(end, start -1, -1):
                if duration > 0:
                    if not using_time[t]:
                        using_time[t] = 1
                        duration -= 1
                else:
                    break

        return sum(using_time)


if __name__ == '__main__':
    test = Solution()
    answer = test.findMinimumTime([[2,3,1],[4,5,1],[1,5,2]])
    print(answer)
    answer = test.findMinimumTime([[1,3,2],[2,5,3],[5,6,2]])
    print(answer)
    answer = test.findMinimumTime([[1,18,5],[3,15,1]])
    print(answer)
