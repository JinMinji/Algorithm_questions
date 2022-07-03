def solution(n, horizontal):
    answer = [[-1 for i in range(n)] for i in range(n)]

    cur = 1
    i = 0
    j = 0
    max_val = 0
    while cur <= n * n:
        # print(max_val, i, j, cur)
        answer[i][j] = cur
        if cur > n * n:
            break

        if cur >= (max_val+1) ** 2:  # max*max 만큼의 공간을 다 청소했으면,
            # 수평, 수직 설정값에 따라 한칸 이동한다.
            if horizontal:
                j += 1
                horizontal = False
            else:
                i += 1
                horizontal = True

            # print(max_val, "+1")
            max_val += 1

        else:
            if i < max_val and j == max_val:  # 상하 이동
                if i-1 >= 0 and answer[i - 1][j] == -1:  # 수평이동 후 수직 아래로 진행할 때
                    i -= 1
                else:  # 수직이동후 오른쪽으로 수평이동, 후 수직 위로 진행할 때
                    i += 1
            elif i == max_val and j == max_val:  # max, max 꼭지점에서 방향설정
                if answer[i - 1][j] == -1:  # 위로 진행
                    i -= 1
                else:  # 좌로 진행
                    j -= 1
            else:  # if i == max_val and j < max_val: # 좌우 이동
                if j != 0 and answer[i][j - 1] == -1:  # 왼쪽으로 진행
                    j -= 1
                else:  # 오른쪽으로 진행
                    j += 1

        cur += 1

    return answer


if __name__ == "__main__":
    print(solution(4, True))
    print(solution(5, False))