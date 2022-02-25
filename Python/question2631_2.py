# 줄세우기
dp = list()

if __name__ == '__main__':
    N = int(input())

    dp = [1 for i in range(N)]
    dp[0] = 1

    children_queue = list()

    for i in range(N):
        children_queue.append(int(input()))

    for i in range(N):
        for j in range(i):
            if children_queue[j] < children_queue[i]:
                dp[i] = max(dp[i], dp[j]+1)


    result = N - max(dp)

    print(result)