#숫자고르기, 골드 5
#완벽한 사이클을 가진 노드 찾기

def cycle_check(num, visited):
    global result
    to_visit = list()
    to_visit.extend(same_list[num])

    while to_visit:
        n = to_visit.pop()
        if n not in visited:
            visited.append(n)
            cycle_check(n, visited)
            visited.pop()

        else:
            idx = visited.index(n)
            for v in visited[idx:]:
                if v not in result:
                    result.append(v)

            return


if __name__ == "__main__":
    N = int(input())

    same_list = [[] for i in range(N+1)]

    for i in range(1, N+1):
        n = int(input())
        same_list[n].append(i)  #단방향 그래프

    # print(same_list)

    result = list()
    for i in range(N+1):
        cycle_check(i, [])

    result.sort()
    print(len(result))
    for r in result:
        print(r)
