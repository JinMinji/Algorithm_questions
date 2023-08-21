def solution(info, query):
    members = []
    for i in info:
        members.append(list(i.split()))
    answer = []

    for i in query:
        lst_que = list(i.split(" "))

        while lst_que.count("and") != 0:
            lst_que.remove("and")
        count = 0

        for member in members:
            tf = True
            if int(member[-1]) >= int(lst_que[-1]):
                for i in range(len(lst_que) - 1):
                    if member[i][0] != lst_que[i][0] and lst_que[i] != '-':
                        tf = False
                        break
            else:
                tf = False

            if tf == True:
                count += 1
        answer.append(count)

    return answer
info = ["java backend junior pizza 150","python frontend senior chicken 210","python frontend senior chicken 150","cpp backend senior pizza 260","java backend junior chicken 80","python backend senior chicken 50"]
query = ["java and backend and junior and pizza 100","python and frontend and senior and chicken 200","cpp and - and senior and pizza 250","- and backend and senior and - 150","- and - and - and chicken 100","- and - and - and - 150"]

print(solution(info, query)