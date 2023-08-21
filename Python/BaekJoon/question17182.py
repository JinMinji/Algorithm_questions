#우주 탐사선
N, K = 0, 0
planet_map = list()
result = 1000000


def dfs(cur_loc, visited, cur_total):
    global result

    if 0 not in visited:
        result = min(result, cur_total)
        return

    for n in range(N):
        if visited[n] == 0:
            cur_total += planet_map[cur_loc][n]

            visited[n] = 1
            dfs(n, visited, cur_total)
            cur_total -= planet_map[cur_loc][n]
            visited[n] = 0


if __name__ == '__main__':
    N, K = map(int, input().split(' '))

    for _ in range(N):
        planet_map.append(list(map(int, input().split(' '))))

    # 플로이드-와샬
    for k in range(len(planet_map)):
        for i in range(len(planet_map)):
            for j in range(len(planet_map)):
                if planet_map[i][k]+planet_map[k][j] < planet_map[i][j]:
                    planet_map[i][j] = planet_map[i][k]+planet_map[k][j]

    # for _ in range(N):
    #     print(planet_map[_])

    cur_loc = K

    visited = [0 for i in range(N)]
    visited[K] = 1

    dfs(K, visited, 0)

    print(result)



