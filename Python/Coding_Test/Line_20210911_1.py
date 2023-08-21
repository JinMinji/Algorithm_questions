def solution(student, k):
    answer = 0
    for i in range(len(student)):
        cnt = 0
        for j in range(i, len(student)):
            if student[j] == 1:
                cnt += 1
                if cnt == k:
                    answer += 1
                    for _ in range(j + 1, len(student)):
                        if student[_] == 0:
                            answer += 1
                        else:
                            break
                    break

    return answer


if __name__ == '__main__' :
    print(solution([0, 1, 0, 0, 1, 1, 0], 2))