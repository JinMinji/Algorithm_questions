def bin_search(lst, num):
    start = 0
    end = len(lst)-1

    answer = 0
    while start <= end:
        mid = (start + end) // 2

        if lst[mid] < num:
            answer = mid
            end = mid -1
        else:
            start = mid +1

    return answer

def solution(stats):
    answer = 0
    team_max = []
    for i in range(len(stats)):
        # print(team_max)
        if team_max:
            if team_max[-1] < stats[i]:
                target = bin_search(team_max, stats[i])
                team_max.pop(target)
                team_max.append(stats[i])
                team_max.sort(reverse=True)
                continue

        team_max.append(stats[i])

    # print(team_max)
    answer = len(team_max)

    return answer