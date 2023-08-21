#알약, 골드5
#이것도 DP야??????
#나 DP 진짜.. 싫어.

def capsule_dp(n):
    global dp
    if dp[n] != 0:
        return dp[n]
    if n == 1:
        dp[n] = 1
        return dp[n]

    elif n%2 == 0:
        dp[n] = capsule_dp(n-1)*2
        return dp[n]

    else:
        dp[n] = capsule_dp(n-1)*2 + (n//2)
        return dp[n]


if __name__ == "__main__":
    dp = [0 for i in range(31)] #알약 개수는 max가 30
    while True:
        N = int(input())    #알약개수
        if N == 0:
            break
        print(capsule_dp(N))
