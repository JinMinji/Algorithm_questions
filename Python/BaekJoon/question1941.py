# 20210527 소문난 칠공주

# S : 이다솜파
# Y : 임도연파
# S가 4명 이상

dx = [0,0,1,-1] # 좌, 우, 상, 하
dy = [-1,1,0,0]

def isPossible(x,y):
    return 0<=x<5 and 0<=y<5

def find_mem(start, mem, S_cnt):
    global cnt_ways
    i, j = start
    if len(mem) == 7:
        if S_cnt >= 4:
            cnt_ways += 1
        return

    for _ in range(4):
        x = i + dx[_]
        y = j + dy[_]
        if isPossible(x, y) and [x,y] not in mem:  # 범위를 벗어나지 않고, 방문하지 않은 학생
            if class_map[x][y] == 'S':  # 이다솜파
                if [x, y] not in used_S_list:  # 이미 기준으로 탐색했던 S면, 못감. 아닐경우만
                    S_cnt += 1
                    mem.append([x, y])
                    find_mem([x, y], mem, S_cnt)
                    S_cnt -= 1
                    mem.pop()
            else:  # 'Y' : 임도연파
                mem.append([x, y])
                find_mem([x, y], mem, S_cnt)
                mem.pop()

def make_7Princess():
    global cnt_ways, S_list, used_S_list
    cnt_ways = 0

    while len(S_list) >= 4:  # 'S' 부터 탐색! 탐색 대상에 걸리는 S가 4개 미만이면, 어차피 안되니까 탐색 중지
        mem = list()  # 탐색을 돌면서 만난 학생. max : 7 (칠공주)
        S_cnt = 0  # 만난 학생 중 'S' 이다솜파 학생 수, min : 4 (이다솜파 4명이상)

        i, j = S_list.pop(0)
        used_S_list.append([i,j])
        mem.append([i,j])
        S_cnt += 1

        find_mem([i, j], mem, S_cnt)

    return cnt_ways

if __name__ == '__main__':
    class_map = list()
    for i in range(5):
        class_map.append(input())
# 입력 : class_map

    global  S_list, used_S_list
    S_list = list()  # 'S'를 기준으로 탐색을 시작할 것이므로 S의 좌표들을 넣어줄 리스트.
    used_S_list = list()  # 기준으로 탐색을 완료한 'S'는 이후 탐색에서 중복으로 세지 않기 위해 아예 못가게 처리할 것.

    for i in range(5):  # 'S' 위치 담기
        for j in range(5):
            if class_map[i][j] == 'S':
                S_list.append([i, j])


    result = make_7Princess()

    print(result)