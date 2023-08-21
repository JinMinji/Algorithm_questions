def solution(logs):
    answer = 0
    for i in range(len(logs)):
        if len(logs[i]) > 100:
            print('길이', logs[i])
            answer += 1
            continue

        if logs[i].count(' ') != 11:  # 공백 개수 11개여야 함
            print('공백 개수', logs[i])
            answer += 1
            continue
        log_list = list(logs[i].split(' '))

        if logs[i].count(':') != 4:  # ':' 개수 4개여야 함
            print(': 개수', logs[i])
            answer += 1
            continue

        while ':' in log_list:
            log_list.remove(':')
        # 조건을 만족하는 로그라면,
        # len : 8
        # [0] = 'team_name'
        # [1] = t
        # [2] = 'application_name'
        # [3] = a
        # [4] = 'error_level'
        # [5] = e
        # [6] = 'message'
        # [7] = m

        if len(log_list) != 8:
            print('항목 개수 틀림', logs[i])
            answer += 1
            continue

        if log_list[0] != 'team_name' or log_list[2] != 'application_name' or log_list[4] != 'error_level' or log_list[6] != 'message':
            # print('항목 없음', logs[i])
            answer += 1
            continue

        isBreak = False
        for v in range(1, 8, 2):
            for w in range(len(log_list[v])):
                # 소문자, 대문자 확인
                if not (65 <= ord(log_list[v][w]) <= 90 or 97 <= ord(log_list[v][w]) <= 122):
                    print('소문자, 대문자', logs[i])
                    answer += 1
                    isBreak = True
                    break

            if isBreak:
                break

    return answer


if __name__ == '__main__':
    # print(solution(["team_name : db application_name : dbtest error_level : info message : test", "team_name : test application_name : I DONT CARE error_level : error message : x", "team_name : ThisIsJustForTest application_name : TestAndTestAndTestAndTest error_level : test message : IAlwaysTestingAndIWillTestForever", "team_name : oberervability application_name : LogViewer error_level : error"]))
    print(solution(["team_name : MyTeam application_name : YourApp error_level : info messag : IndexOutOfRange", "no such file or directory", "team_name : recommend application_name : recommend error_level : info message : RecommendSucces11", "team_name : recommend application_name : recommend error_level : info message : Success!", "   team_name : db application_name : dbtest error_level : info message : test", "team_name     : db application_name : dbtest error_level : info message : test", "team_name : TeamTest application_name : TestApplication error_level : info message : ThereIsNoError"]))



