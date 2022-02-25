#불량이용자

def solution(id_list, report, k):
    answer = [0 for i in range(len(id_list))]
    report_cnt = [[] for i in range(len(id_list))]
    for i in range(len(report)):
        from_id, to_id = report[i].split(' ')
        report_cnt[id_list.index(to_id)].append(from_id)

    for i in range(len(report_cnt)):
        report_cnt[i] = list(set(report_cnt[i]))    #중복제거
        if len(report_cnt[i]) >= k:
            for _ in report_cnt[i]:
                answer[id_list.index(_)] += 1

    return answer


if __name__ == '__main__':
    print(solution(["muzi", "frodo", "apeach", "neo"], ["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"], 2))