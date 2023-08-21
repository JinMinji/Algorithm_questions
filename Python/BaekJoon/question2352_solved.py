# 20210507 반도체설계

def solution(N, port_input):
    # N = int(input())
    #
    # port_input = list(map(int, input().split()))
    dp = [port_input[0]]
    result = 0

    for i in range(len(port_input)):
        #안 꼬였을 때
        if port_input[i] > dp[result]:
            dp.append(port_input[i])
            result += 1

        #꼬였을 때
        else:
            for j in range(result):
                if j == result - 1:
                    dp[j] = port_input[i]
                    break
                if dp[j] <= port_input[i] and port_input[i] < dp[j+1]:
                    dp[j+1] = port_input[i]
                    break
    return result

def lower_bound(arr, val):
    global ans
    for idx in range(0, len(arr)):
        if idx == len(arr) - 1:
            return idx
        if arr[idx] <= val < arr[idx + 1]:
            return idx + 1

def test_solution(n, port_list):
    tmp_list = [-1]
    ans = 0
    for i in range(n):
        if tmp_list[-1] < port_list[i]:
            tmp_list.append(port_list[i])
            ans += 1
        else:
            tmp_list[lower_bound(tmp_list, port_list[i])] = port_list[i]
    return ans

if __name__ == "__main__":
    N = 6
    port_input = [4, 2, 6, 3, 1, 5]

    print(solution(N, port_input))
    print(test_solution(N, port_input))
