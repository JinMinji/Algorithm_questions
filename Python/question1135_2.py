# 뉴스 전하기, 골드 1
def get_dp(n):
    global dp, tree
    if dp[n] != -1:
        return dp[n]
    else:
        if not tree[n]:
            dp[n] = 0
            return dp[n]
        else:
            tmp_list = list()
            for i in range(len(tree[n])):
                tmp_list.append(get_dp(tree[n][i]))

            tmp_list.sort(reverse=True)

            max_time = 0
            for i in range(len(tmp_list)):
                max_time = max(max_time, tmp_list[i]+i+1)

            dp[n] = max_time
            return dp[n]


if __name__ == '__main__':
    N = int(input())

    seniors = list(map(int, input().split()))

    tree = [[] for i in range(N)]

    for i in range(1, len(seniors)):
        tree[seniors[i]].append(i)

    dp = [-1 for i in range(len(seniors))]

    print(get_dp(0))