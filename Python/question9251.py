#LCS, 골드5


if __name__ == "__main__":
    a_str = input()
    b_str = input()

    dp = [[0 for i in range(len(b_str)+1)] for i in range(len(a_str)+1)]

    result = 0
    for i in range(1, len(a_str)+1):
        for j in range(1, len(b_str)+1):
            if a_str[i-1] == b_str[j-1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    # print(dp)
    print(dp[len(a_str)][len(b_str)])