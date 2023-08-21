dp = list()
team_list = list()
child_teams = dict()


def total_mem(team_id):  # 팀 ID를 입력하면, 그 팀의 총인원수를 반환해주는 함수
    ID = int(team_id)
    if dp[ID] != -1:
        return dp[ID]
    else:
        tmp = int(team_list[ID][3])
        for c in child_teams.get(str(ID), []):
            tmp += total_mem(c)

        dp[ID] = tmp

    return dp[ID]


def solution(csv_string, keyword):
    global team_list
    team_list = csv_string.split('\n')
    for i in range(len(team_list)):
        t = list(map(str, team_list[i].split(',')))
        team_list[i] = t
    searched_list = []
    print(csv_string)

    # child_teams = dict()    #현재 입력값은, 상위팀만 가지고있으나,
    # 하위조직 인원을 구하기에는 하위조직정보를 가진 리스트가 필요하다.
    global child_teams

    for i in range(1, len(team_list)):  # 0인덱스는 제외
        if team_list[i][2] != '':
            child_teams[team_list[i][2]] = child_teams.get(team_list[i][2], [])
            child_teams[team_list[i][2]].append(team_list[i][0])

        if keyword in team_list[i][1]:  # 조직명에 포함되었을 경우, 검색결과 리스트에 ID를 넣는다.
            searched_list.append(team_list[i][0])

    global dp
    dp = [-1 for i in range(len(team_list))]

    answer = 0
    for i in searched_list:
        answer += total_mem(i)

    return answer

if __name__ == '__main__':
    a = '조직 ID,조직명,상위 조직 ID,소속 팀원 수\n1,토스팀,,1\n2,인터널 트라이브,1,1\n3,인터널 매니저 팀,2,7\n4,비바 플랫폼 팀,2,14\n5,아웃터널 트라이브,1,2\n6,가이드 팀,5,4\n7,피트아웃 사일로,5,11'
    b = '아웃'

    print(solution(a, b))

