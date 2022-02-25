# 순위검색

def solution(info, query):
    info_arr = list()

    for i in range(len(info)):
        person = list(info[i].split(' '))
        info_arr.append(person)

    answer = []

    for i in range(len(query)): # 쿼리 질문을 돌면서
        q = list(query[i].split(' and '))
        tmp = q.pop()
        q.extend(tmp.split(' '))
        cnt = 0
        for j in range(len(info_arr)):  # 각 사람들의 인포를 돌면서
            sameYN = True
            for k in range(4):  # 인포 속 값들을 돌면서
                if q[k] != '-' and info_arr[j][k] != q[k]:
                    sameYN = False
                    break
            if q[4] != '-' and int(info_arr[j][4]) < int(q[4]):
                sameYN = False

            if sameYN:
                cnt += 1

        answer.append(cnt)

    return answer


if __name__ == '__main__':
    print(solution(["java backend junior pizza 150","python frontend senior chicken 210","python frontend senior chicken 150","cpp backend senior pizza 260","java backend junior chicken 80","python backend senior chicken 50"], ["java and backend and junior and pizza 100","python and frontend and senior and chicken 200","cpp and - and senior and pizza 250","- and backend and senior and - 150","- and - and - and chicken 100","- and - and - and - 150"]))
