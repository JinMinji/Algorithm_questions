# 네이버 2021 상반기 1번 기출과 동일
# 프로그래머스 위클리챌린지 2주차 상호평가

def solution(scores):
    answer = ''
    tmp_avg = list()
    tmp_scores = list()

    for j in range(len(scores)):
        tmp = list()
        for i in range(len(scores)):
            tmp.append(scores[i][j])

        tmp_scores.append(tmp)

    for i in range(len(tmp_scores)):
        if tmp_scores[i].count(tmp_scores[i][i]) == 1:  #유일한 점수
            if max(tmp_scores[i]) == tmp_scores[i][i] or min(tmp_scores[i]) == tmp_scores[i][i]:
                tmp_scores[i][i] = 0
                tmp_avg.append(sum(tmp_scores[i])/(len(tmp_scores[i])-1))
                continue

        tmp_avg.append(sum(tmp_scores[i]) / len(tmp_scores[i]))

    print(tmp_avg)
    for i in range(len(tmp_avg)):
        if tmp_avg[i] >= 90:
            answer += 'A'
        elif tmp_avg[i] >= 80:
            answer += 'B'
        elif tmp_avg[i] >= 70:
            answer += 'C'
        elif tmp_avg[i] >= 50:
            answer += 'D'
        else:
            answer += 'F'

    return answer

if __name__ == '__main__':
    print(solution([[100,90,98,88,65],[50,45,99,85,77],[47,88,95,80,67],[61,57,100,80,65],[24,90,94,75,65]]))