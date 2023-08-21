# 20210628 양구출작전

def save_sheep():
    answer = 0
    for i in range(2, N+1):
        if leaf_check[i] == 1:
            now_sheep = 0
            now = i
            while now != 1:     #각 섬에서 1번에 도달할 때까지.
                if bridges[now] == 1:   # 1번 섬에 도착! save
                    if island_info[now] >= 0: #양 섬
                        now_sheep += island_info[now]
                        island_info[now] = 0  # 구했으니 섬에 남은 양은 0

                    else : #늑대섬
                        now_sheep += island_info[now]
                        if now_sheep < 0:
                            now_sheep = 0

                else: # 가는길.
                    if island_info[now] >= 0:  # 양 섬
                        now_sheep += island_info[now]
                        island_info[now] = 0  # 이동했으니 섬에 남은 양은 0
                    else:   #늑대섬
                        now_sheep += island_info[now]   #이미 - 값이 들어있으니까, 더해준다
                        if now_sheep < 0:
                            now_sheep = 0

                now = bridges[now]  #다음섬으로

            answer += now_sheep

    return answer


if __name__ == '__main__':
    N = int(input())
    island_info = [0 for _ in range(N+1)]
    bridges = dict()
    leaf_check = [0 for _ in range(N+1)]
    for i in range(2, N+1):
        type_of_island, num_of_animals, to_island = map(str, input().split())
        if type_of_island == 'W':
            island_info[i] = - int(num_of_animals)
        else:
            island_info[i] = int(num_of_animals)

        bridges[i] = int(to_island)
        leaf_check[i] += 1
        leaf_check[int(to_island)] += 1

    print(save_sheep())
