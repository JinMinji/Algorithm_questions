def search(start, cur):
    global answer, a_arr, b_arr

    if sum(a_arr[start:cur + 1]) >= sum(b_arr[start:cur + 1]):
        answer += cur - start
        a_arr[cur] = sum(a_arr[start:cur + 1]) - sum(b_arr[start:cur])
        for i in range(start, cur):
            a_arr[i] = b_arr[i]

    else:
        search(start, cur + 1)


def solution(arr, brr):
    global answer, a_arr, b_arr
    answer = 0
    a_arr = arr
    b_arr = brr

    # A가 작을 때
    # 1. B에서 가져오는 것만으로도 A의 크기를 맞출 수 있는 경우
    # 2. B에서 가져오는 걸로 부족해서 다른 셀의 너비도 빌려와야하는 경우
    # A가 클 때
    # 1. B쪽으로 넘긴다.

    # 계속 -> 방향으로 확인해서 체크하면 좋겠는데..!

    for i in range(len(a_arr) - 1):  # 마지막 셀은 자동으로 맞춰질 것이므로, 체크 안함
        if a_arr[i] == b_arr[i]:
            continue

        if a_arr[i] < b_arr[i]:
            if a_arr[i] + a_arr[i + 1] >= b_arr[i] + b_arr[i + 1]:
                a_arr[i + 1] -= b_arr[i] - a_arr[i]
                a_arr[i] = b_arr[i]
                answer += 1

            else:  # 빌려올 곳 탐색
                search(i, i + 1)

        else:
            a_arr[i + 1] += a_arr[i] - b_arr[i]
            a_arr[i] = b_arr[i]
            answer += 1

    return answer


if __name__ == '__main__':
    print(solution([3, 7, 2, 4], [4, 5, 5, 2]))
    print(solution([6, 2, 2, 6], [4, 4, 4, 4]))
    print(solution([1, 1, 4, 2], [2, 1, 1, 4]))