from collections import defaultdict

logs = ["0001 3 95", "0001 5 90", "0001 5 100", "0002 3 95", "0001 7 80", "0001 8 80", "0001 10 90", "0002 10 90", "0002 7 80", "0002 8 80", "0002 5 100", "0003 99 90"]


answer = ["None"]

examinee = defaultdict(list)

for log in logs:
    solved_question = list(log.split(' '))
    examinee[solved_question[0]].append([int(solved_question[1]), int(solved_question[2])])


solved_num = [[] for i in range(101)]

for mem in examinee:
    examinee[mem].sort(key=lambda x:(x[0],-x[1]))

    q_num = examinee[mem][0]
    result = []

    for i in examinee[mem]:
        if i[0] != q_num:
            result.append(i)
            q_num = i[0]

    examinee[mem] = result

    if len(examinee[mem]) >= 5:
        solved_num[len(examinee[mem])].append(mem)

for i in range(5,101):
    if len(solved_num[i]) == 2:
        if examinee[solved_num[i][0]] == examinee[solved_num[i][1]]:
            answer = [solved_num[i][0], solved_num[i][1]]

    if len(solved_num[i]) >= 2:
        if examinee[solved_num[i][0]] == examinee[solved_num[i][1]]:
            answer = [solved_num[i][0], solved_num[i][1]]
        for j in range(2,len(solved_num[i])):
            if examinee[solved_num[i][0]] == examinee[solved_num[i][j]]:
                answer.append(solved_num[i][j])

#다른 테스트케이스는 맞추지 못함!
print(answer)
