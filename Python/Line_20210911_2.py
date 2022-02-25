def solution(research, n, k):
    answer = 'None'
    cnt_table = dict()
    # 검색어별, 일자별 검색횟수를 가지고 있는 dict -> {a:{1:5, 2:3, 3:7, 4:1}, b: ...}

    for i in range(len(research)):
        for j in range(len(research[i])):
            cnt_table[research[i][j]] = cnt_table.get(research[i][j], [0 for i in range(len(research))])
            cnt_table[research[i][j]][i] += 1

    tmp_ans = [0, 'None']
    for key, value in cnt_table.items():
        cnt = 0
        for i in range(len(value)-n+1):   # value의 인덱스 0에는 아무것도 들어있지 않음
            isIssue = True
            tmp_cnt = 0
            for _ in range(n):
                tmp_cnt += value[i+_]
                if value[i+_] < k:
                    isIssue = False
                    break
            if isIssue and tmp_cnt >= 2*n*k:
                cnt += 1

        if cnt > 0:
            if tmp_ans[0] < cnt:
                tmp_ans = [cnt, key]
            elif tmp_ans[0] == cnt and ord(tmp_ans[1]) > ord(key):
                tmp_ans = [cnt, key]

    answer = tmp_ans[1]

    return answer


if __name__ == '__main__':
    # print(solution(["abaaaa","aaa","abaaaaaa","fzfffffffa"], 2, 2))
    # print(solution(["yxxy","xxyyy"], 2, 1))
    print(solution(["yxxy","xxyyy","yz"], 2, 1))
    print(solution(["xy","xy"], 1, 1))
