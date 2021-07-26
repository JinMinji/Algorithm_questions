#20210719 개미굴

def dfs_print(f):


def draw_map(map_info):
    floors = [{} for _ in range(15)]    # max floor = 15
    # insert
    for r in range(len(map_info)):

        cur_feeds = list(floors[0].keys())   # 첫 층의 key값들 = 첫 층에 있는 먹이들 (시작)

        for f in range(len(map_info[r])):   # 층을 모두 돌면서, 경로를 찾아준다.
            cur_val = map_info[r][f]        # 현재 먹이 값.
            if cur_val in cur_feeds:     # 만약 현재 경로에서 가능한 먹이중에, 동일한 값이 있으면  : 이 경로로 계속 탐색해보기.
                cur_feeds = floors[f].get(cur_val, [])   # 다음 가능한 경로를 새로 설정 : 기존 경로대로 따라가보기.

            else:   # 가능한 먹이가 아니면,
                cur_feeds = []    # 가능한 것 없도록 변경 : 다음에 방문할 것이 없도록.

                tmp_next = list()

                if f+1 < len(map_info[r]):
                    tmp_next = map_info[r][f+1]
                else:
                    tmp_next = []

                floors[f][cur_val] = floors[f].get(cur_val, [])
                floors[f][cur_val].append(tmp_next)  # 현재 층에 나를 붙이고, 이후 자료들을 붙여준다!

    # print
    # dfs
    pre_text = ''
    for k in range(len(floors[0])):

        print(pre_text+floors[])


        floors

    print(floors)


if __name__ == '__main__':
    N = int(input())

    informations = list()
    for i in range(N):
        info = list(map(str, input().split()))
        info.pop(0)    # 맨앞에 개수는 빼준다
        informations.append(info)

    draw_map(informations)