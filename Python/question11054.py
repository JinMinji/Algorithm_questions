#가장 긴 바이토닉 부분 수열, 골드 3


if __name__ == "__main__":
    N = int(input())
    input_list = list(map(int, input().split()))

    #DP 배열 만들기
    lis = [1 for i in range(N)] #Longest Increasing Subsequence
    lds = [1 for i in range(N)] #Longest Decreasing Subsequence

    for i in range(1, N):
        for j in range(i):
            if input_list[j] < input_list[i]:
                lis[i] = max(lis[i], lis[j]+1)
            if input_list[-(j+1)] < input_list[-(i+1)]:
                lds[-(i+1)] = max(lds[-(i+1)], lds[-(j+1)]+1)
    #
    # print(lis)
    # print(lds)

    res = 0
    for i in range(N):  # 중심이 i 일때, 바이토닉 수열의 길이
        res = max(res, lis[i] + lds[i])

    print(res - 1)  # 중심으로 선택된 인덱스를 두번 세니까, 한번은 빼준다.

