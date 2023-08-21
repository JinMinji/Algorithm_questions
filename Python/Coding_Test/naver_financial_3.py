def solution(logs):
    answer = []
    examinee = dict()
    for i in range(len(logs)):
        exam_num, ques_num, score = logs[i].split()
        examinee[exam_num] = examinee.get(exam_num, [-1 for i in range(101)])
        examinee[exam_num][int(ques_num)] = score    #마지막 제출 결과가 점수.

    num_list = []
    score_list = []
    for key, value in examinee.items():
        num_list.append(key)
        score_list.append(value)

    for i in range(len(num_list)):
        if num_list[i] not in answer:
            for j in range(i+1, len(num_list)):
                if score_list[i] == score_list[j] and score_list[i].count(-1) <= 96:
                    if num_list[i] not in answer:
                        answer.append(num_list[i])
                    answer.append(num_list[j])

    if len(answer) == 0:
        return ['None']

    answer.sort()
    return answer


if __name__ == '__main__':
    # print(solution(["0001 3 95", "0001 5 90", "0001 5 100", "0002 3 95", "0001 7 80", "0001 8 80", "0001 10 90", "0002 10 90", "0002 7 80", "0002 8 80", "0002 5 100", "0003 99 90"]))
    print(solution(["1901 10 50", "1909 10 50"]))