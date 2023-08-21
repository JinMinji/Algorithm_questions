#텀프로젝트

def dfs(v):
    global result
    visited[v] = 1
    route.append(v)

    # print(v, route)

    n = students[v]

    if visited[n] == 1:     # 순환함
        if n in route:   # 순환한 부분까지 잘라서 한 팀. 팀에 속한 사람들 다 넣어주기
            result += route[route.index(n):]
        return
    else:   # 계속 찾기
        dfs(n)


if __name__ == '__main__':
    T = int(input())

    result_list = list()

    for t in range(T):
        N = int(input())
        students = [0] + list(map(int, input().split(' ')))

        visited = [0 for i in range(N+1)]
        result = list()
        for i in range(1, N+1):
            if visited[i] == 0:
                route = list()  # 새 팀
                dfs(i)

        result_list.append(N - len(result))

    for r in result_list:
        print(r)