# 승부 예측 골드 3

def match(n, p):
    global result, nations

    if n == 6:  # 조별리그 종료
        result.sort(key=lambda x: x[0])

        # 4 국가 동점일 때

        # 3 국가가 동점일 때

        # 1위는 정해졌고, 나머지 3국가가 동점일 때

        # 1위는 정해졌고, 나머지 2국가가 동점일 때


    # 조별리그 진행중

    # A가 승리
    result[nations.index(input_list[i][0])] += 3
    match(2, p * input_list[i][2])
    result[nations.index(input_list[i][0])] -= 3

    # 무승부
    result[nations.index(input_list[i][0])] += 1
    result[nations.index(input_list[i][1])] += 1
    match(2, p * input_list[i][3])
    result[nations.index(input_list[i][0])] -= 1
    result[nations.index(input_list[i][1])] -= 1

    # A가 패배
    result[nations.index(input_list[i][1])] += 3
    match(2, p * input_list[i][4])
    result[nations.index(input_list[i][1])] -= 3


if __name__ == '__main__':
    nations = list(map(str, input().split(' ')))

    input_list = list()

    for _ in range(6):
        input_list.append(list(map(str, input().split(' '))))

    result = [0 for i in range(4)]

    match(0, 1)

    for i in range(4):
        print(format(result[i], "0.6f"))
