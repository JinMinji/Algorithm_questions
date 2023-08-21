def bfs(question):
    pass


def solution(alp, cop, problems):
    # 도달해야하는 알고력과 코딩력.
    # 문제를 모두 풀 필요는 없지만,
    # 문제를 모두 풀 수는 있는 알고력과 코딩력을 쌓아야하는 문제
    problems.sort(key=lambda x: x[0])
    target_alp = problems[-1][0]
    problems.sort(key=lambda x: x[1])
    target_cop = problems[-1][1]

    dp_time = [[300 for i in range(target_cop + 1)] for i in range(target_alp + 1)]
    # dp_time[a][b] 알고력 a, 코딩력 b에 도달하기 위한 최소시간.
    # alp_req, cop_req의 max는 150 이므로 answer의 max는 300

    # 그냥 공부하는 경우 -> [0, 0, 1, 0, 1], [0, 0, 0, 1, 1]
    problems.append([0, 0, 1, 0, 1])
    problems.append([0, 0, 0, 1, 1])

    queue = list()

    if alp >= target_alp and cop >= target_cop:
        return 0

    for q in problems:  # 맨 처음, 풀 수 있는 문제들 queue에 넣기
        if q[0] <= alp and q[1] <= cop:
            queue.append([alp, cop, 0, q])

    while queue:
        cur_alp, cur_cop, cur_cost, tmp = queue.pop(0)
        al = min(cur_alp + tmp[2], target_alp)
        co = min(cur_cop + tmp[3], target_cop)

        if dp_time[al][co] < cur_cost + tmp[4]:
            continue
        else:
            dp_time[al][co] = cur_cost + tmp[4]

        if al >= target_alp and co >= target_cop:
            print("here", cur_alp, cur_cop, cur_cost, tmp)
            continue

        for q in problems:  # 맨 처음, 풀 수 있는 문제들 queue에 넣기
            if q[0] <= al and q[1] <= co:
                queue.append([al, co, cur_cost + tmp[4], q])

        for _ in range(len(dp_time)):
            print(dp_time[_])

        print()

        # if dp_time[target_alp][target_cop] != 300:
        #     break

    return dp_time[target_alp][target_cop]


if __name__ == "__main__":
    print(solution(0, 0, [[0,0,2,1,2],[4,5,3,1,2],[4,11,4,0,2],[10,4,0,4,2]]))