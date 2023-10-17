# Contest361, Q1

class Solution:
    def countSymmetricIntegers(self, low: int, high: int) -> int:
        max_len = len(str(high))
        min_len = len(str(low))
        answer = 0
        if min_len <= 2:
            for i in range(1, 10):
                tmp = i*10 + i
                if low <= tmp <= high:
                    answer += 1

        if max_len >= 4:
            for i in range(10, 100):
                for j in range(1, 100):
                    if i//10 + i-(i//10)*10 == j//10 + j-(j//10)*10:
                        if low <= i*100 + j <= high:
                            # print(i, j)
                            answer += 1

        return answer


if __name__ == "__main__":
    test = Solution()
    print(test.countSymmetricIntegers(low = 1, high = 100))
    print(test.countSymmetricIntegers(low = 1200, high = 1230))
    print(test.countSymmetricIntegers(10, 11))
    print(test.countSymmetricIntegers(100, 10000))

