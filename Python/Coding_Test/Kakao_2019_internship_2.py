def solution(s):
    s = s[1:-2]
    tmp_set = s.split('},') # 일단 string으로 받은 거 list로 변환
    input_set = [[] for i in range(len(tmp_set))]
    for i in range(len(tmp_set)):
        tmp_set[i] = tmp_set[i][1:]
        tmp_set[i] = list(map(int, tmp_set[i].split(',')))

        input_set[len(tmp_set[i])-1] = tmp_set[i]

    visited = list()
    for i in range(len(input_set)):
        for j in range(len(input_set[i])):
            if input_set[i][j] not in visited:
                visited.append(input_set[i][j])
                break

    answer = visited
    return answer


if __name__ == '__main__':
    print(solution("{{2},{2,1},{2,1,3},{2,1,3,4}}"))
    print(solution("{{1,2,3},{2,1},{1,2,4,3},{2}}"))
