def solution(num_teams, remote_tasks, office_tasks, employees):
    answer = []
    team_office = [[False, 0] for i in range(num_teams)]

    for i in range(len(employees)):
        tmp_list = employees[i].split(' ')
        remote = True
        team_num = int(tmp_list[0]) - 1  # 팀번호도 1부터 시작하므로, 인덱스로 맞춰주기위해 -1
        for j in range(1, len(tmp_list)):
            if tmp_list[j] in office_tasks:
                team_office[team_num][0] = True  # 사원번호는 1부터 시작
                remote = False
                break

        if remote:
            answer.append(i + 1)
            if team_office[team_num][0] == False and team_office[team_num][1] == 0:
                team_office[team_num][1] = i + 1

    for i in range(len(team_office)):
        if not team_office[i][0]:
            answer.remove(team_office[i][1])

    return answer


if __name__ == '__main__':
    print(solution(3, ["development","marketing","hometask"], ["recruitment","education","officetask"], ["1 development hometask","1 recruitment marketing","2 hometask","2 development marketing hometask","3 marketing","3 officetask","3 development"]))
    print(solution(2, ["design"], ["building","supervise"], ["2 design","1 supervise building design","1 design","2 design"]))