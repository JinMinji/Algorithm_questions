result = list()


def find_ways(id_list, n, visited):
    global result
    if n == len(id_list):
        result.append(visited)
        return
    for i in range(len(id_list[n])):
        if id_list[n][i] not in visited:
            visited.append(id_list[n][i])
            find_ways(id_list, n+1, visited)
            visited.pop()


def solution(user_id, banned_id):
    available = list()

    for ban in banned_id:
        avail = []
        for user in user_id:
            if len(user) == len(ban):
                for i in range(len(user)):
                    if user[i] != ban[i] and ban[i] != '*':
                        break
                    if i == len(user)-1:
                        avail.append(user)
        available.append(avail)

    for i in range(len(available[0])):
        visited = [i]
        find_ways(available, 1, visited)

    tmp_set = set(result)

    answer = len(list(tmp_set))

    return answer


if __name__ == '__main__':
    # print(solution(["frodo", "fradi", "crodo", "abc123", "frodoc"], ["fr*d*", "abc1**"]))
    print(solution(["frodo", "fradi", "crodo", "abc123", "frodoc"], ["fr*d*", "*rodo", "******", "******"]))
