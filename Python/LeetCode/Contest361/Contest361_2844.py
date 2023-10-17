# Contest361, Q2

class Solution:
    def minimumOperations(self, num: str) -> int:
        answer = len(num)
        targets = ["00", "25", "50", "75"]

        if len(num) == 1 and num != "0":
            return 1

        for k in range(len(targets)):
            target = targets[k]
            cnt = 0
            idx = 1
            for i in range(len(num)):
                if num[-(i+1)] == target[-idx]:
                    idx += 1
                    if idx > 2:
                        answer = min(answer, cnt)
                        break
                else:
                    cnt += 1
            answer = min(answer, cnt+idx-1)
        return answer


if __name__ == "__main__":
    test = Solution()
    # print(test.minimumOperations(num = "2245047"))
    # print(test.minimumOperations(num = "2908305"))
    # print(test.minimumOperations(num = "10"))
    print(test.minimumOperations(num = "15"))

