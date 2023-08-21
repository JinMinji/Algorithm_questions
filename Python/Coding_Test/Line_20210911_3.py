def solution(jobs):
    answer = []
    next_s = 0
    for i in range(1, len(jobs)):
        if jobs[next_s][0] > jobs[i][0]:     # 요청시간이 같은 작업은 없음.
            next_s = i

    answer.append(jobs[next_s][2])          # 처리한 분류번호 순서
    cur_time = 1                            # 현재시간
    cur_time += jobs[next_s][1]
    done = [next_s]

    while len(done) < len(jobs):    # 처리한 작업개수가 전체 작업개수보다 작을 동안
        waiting_list = []
        for i in range(len(jobs)):
            tmp_time = 0
            if i not in done and jobs[i][0] <= cur_time:    # 완료여부, 요청시각 비교
                if jobs[next_s][2] == jobs[i][2]:  # 분류번호가 같을 때
                    tmp_time += jobs[next_s][1]
                    done.append(i)

                else:   # 분류번호가 다를 때
                    waiting_list.append(i)

        if tmp_time > 0:
            cur_time += tmp_time

        else:
            important_scores = [0 for _ in range(100)]  #분류번호 max = 100
            for k in waiting_list:
                important_scores[jobs[k][2]] += jobs[k][3]  # 중요도 더하기

            next_s = important_scores.index(max(important_scores))
            if next_s == 0:
                cur_time += 1

            # elif len(answer) == 0 or (len(answer) > 0 and answer[-1] != next_s):
            else:
                if len(answer) == 0 or (len(answer) > 0 and answer[-1] != next_s):
                    answer.append(next_s)
                for k in waiting_list:
                    if jobs[k][2] == next_s:
                        done.append(k)
                        cur_time += jobs[k][1]

    return answer


if __name__ == '__main__':
    print(solution([[1, 5, 2, 3], [2, 2, 3, 2], [3, 1, 3, 3], [5, 2, 1, 5], [7, 1, 1, 1], [9, 1, 1, 1], [10, 2, 2, 9]]))
    # print(solution([[1, 2, 1, 5], [2, 1, 2, 100], [3, 2, 1, 5], [5, 2, 1, 5]]))
    # print(solution([[0, 2, 3, 1], [5, 3, 3, 1], [10, 2, 4, 1]]))
    # print(solution([[0, 5, 1, 1], [2, 4, 3, 3], [3, 4, 4, 5], [5, 2, 3, 2]]))

