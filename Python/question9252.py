#LCS 2, 골드4
import sys


def find_string(i, j):
    if dp[i][j] == 0:
        return
    if str1[i-1] == str2[j-1]:
        result.append(str1[i-1])
    else:
        if dp[i-1][j] > dp[i][j-1]:
            result.append(str1[i - 1])
        else:
            pass


if __name__ == "__main__":
    str1 = sys.stdin.readline()
    str2 = sys.stdin.readline()

    dp = [[0 for i in range(len(str2))]for i in range(len(str1))]

    for i in range(len(str1)-1):
        for j in range(len(str2)-1):
            if str1[i] == str2[j]:
                dp[i+1][j+1] = dp[i][j]+1
            else:
                dp[i+1][j+1] = max(dp[i][j+1], dp[i+1][j])

    max_len = dp[-1][-1]

    print(max_len)

    for i in range(len(dp)):
        print(dp[i])

    result = []

    find_string(len(str1)-2, len(str2)-2)

    result.reverse()

    print(*result)

