# 오름세, 골드 2

if __name__ == '__main__':
    answer = list()
    while input():

        num_list = list(map(int, input().split(' ')))

        dp = [1 for i in range(len(num_list))]

        for i in range(len(num_list)):
            for j in range(i):
                if num_list[j] < num_list[i]:
                    dp[i] = max(dp[i], dp[j]+1)

        answer.append(max(dp))

    for ans in answer:
        print(ans)
