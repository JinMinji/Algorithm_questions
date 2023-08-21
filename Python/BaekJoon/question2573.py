# 빙산, 골드 4
dx = [0, 0, 1, -1] #동, 서, 남, 븍
dy = [-1, 1, 0, 0] #왼, 오, 하, 상


def bfs_cnt(start, ice):
    visited = [[0 for i in range(M)] for i in range(N)]
    to_visit = list()
    to_visit.append(start)
    tmp_x, tmp_y = start
    visited[tmp_x][tmp_y] = 1
    res = 1

    while to_visit:
        i, j = to_visit.pop()
        for _ in range(4):
            x = i + dx[_]
            y = j + dy[_]
            if 0 <= x < N and 0 <= y < M:
                if ice[x][y] != 0 and visited[x][y] == 0:
                    to_visit.append([x, y])
                    visited[x][y] = 1
                    res += 1

    return res


if __name__ == "__main__":
    N, M = map(int, input().split())

    ice_map = list()

    for i in range(N):  #입력값 받기
        ice_map.append(list(map(int, input().split())))


    #step1 : 빙산을 녹인다
    #빙산
    start_ice = [0, 0]
    total_cnt = 0
    answer = 0
    #처음부터 두 덩이인 경우 체크
    for i in range(N):  # 모든 위치를 돌면서 #n^2
        for j in range(M):
            if ice_map[i][j] != 0:
                total_cnt += 1
                start_ice = [i, j]

    if total_cnt == bfs_cnt(start_ice, ice_map):
        while start_ice != [-1, -1]:
            total_cnt = 0
            answer += 1
            start_ice = [-1, -1]
            tmp_result = [[0 for i in range(M)] for i in range(N)]
            need_bfs = False
            for i in range(N):  # 모든 위치를 돌면서 #n^2
                for j in range(M):
                    if ice_map[i][j] == 0:
                        continue
                    else:
                        cnt = 0
                        for _ in range(4):
                            x = i + dx[_]
                            y = j + dy[_]

                            if 0 <= x < N and 0 <= y < M and ice_map[x][y] == 0:
                                cnt += 1

                        if ice_map[i][j] - cnt <= 0:
                            need_bfs = True
                            tmp_result[i][j] = 0
                        else:
                            total_cnt += 1
                            start_ice = [i, j]
                            tmp_result[i][j] = ice_map[i][j] - cnt

            ice_map = tmp_result

            # step2 : 빙산이 하나라도 0이 된 부분이 있는 단계에서만,
            # for i in range(N):
            #     print(ice_map[i])
            # print()

            if need_bfs:    # 빙산이 분리되지 않았는지 체크한다
                if total_cnt == 0:
                    answer = 0
                    break
                if total_cnt != bfs_cnt(start_ice, ice_map):
                    # print(total_cnt, bfs_cnt(start_ice, ice_map))
                    # -> 전체 빙산의 개수 cnt, 임의의 빙산에서 빙산 bfs한 cnt 값 비교
                    break

    print(answer)
