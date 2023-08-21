def data_lowerbounds(plans, data):
    start = 0
    end = len(plans) - 1

    res_idx = -1

    while start <= end:
        mid = (start + end) // 2
        if plans[mid][0] >= data:
            res_idx = mid
            end = mid - 1
        else:
            start = mid + 1

    return res_idx


def services_lowerbounds(plans, services, service_list):
    start = 0
    end = len(plans) - 1

    res_idx = -1

    while start <= end:
        mid = (start + end) // 2
        flag = True

        for s in services:
            if s not in service_list[:plans[mid][1]]:
                flag = False
                break

        if flag:
            res_idx = mid
            end = mid - 1

        else:
            start = mid + 1

    return res_idx


def solution(n, plans, clients):
    answer = []

    service_lst = list()
    for i in range(len(plans)):
        tmp_plans = list(map(int, plans[i].split()))
        data = tmp_plans.pop(0)
        service_lst.extend(tmp_plans)
        tmp_idx = len(service_lst)
        plans[i] = [data, tmp_idx]

    for i in range(len(clients)):
        tmp_lst = list(map(int, clients[i].split()))

        # print(plans, tmp_lst[1:])

        data_idx = data_lowerbounds(plans, tmp_lst[0])
        services_idx = services_lowerbounds(plans, tmp_lst[1:], service_lst)

        # print(data_idx, services_idx)
        if data_idx == -1 or services_idx == -1:
            answer.append(0)
        else:
            answer.append(max(data_idx, services_idx) + 1)

    return answer


if __name__ == "__main__":
    print(solution(5, ["100 1 3", "500 4", "2000 5"], ["300 3 5", "1500 1", "100 1 3", "50 1 2"]))
    print(solution(4, ["38 2 3", "394 1 4"], ["10 2 3", "300 1 2 3 4", "500 1"]))
