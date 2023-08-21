def solution(ings, menu, sell):
    dict_ings = dict()  # 찾기 쉽도록, dict로 변경
    for i in range(len(ings)):
        tmp = ings[i].split()
        dict_ings[tmp[0]] = int(tmp[1])

    menu_dict = dict()  # 찾기 쉽도록, dict로 변경
    for i in range(len(menu)):
        tmp_info = menu[i].split()
        menu_cost = 0
        for j in tmp_info[1]:
            menu_cost += dict_ings[j]

        menu_dict[tmp_info[0]] = int(tmp_info[2]) - menu_cost

    answer = 0
    for i in range(len(sell)):
        tmp = sell[i].split()
        answer += menu_dict[tmp[0]] * int(tmp[1])

    return answer


if __name__ == '__main__':
    print(solution(["r 10", "a 23", "t 124", "k 9"], ["PIZZA arraak 145", "HAMBURGER tkar 180", "BREAD kkk 30", "ICECREAM rar 50", "SHAVEDICE rar 45", "JUICE rra 55", "WATER a 20"], ["BREAD 5", "ICECREAM 100", "PIZZA 7", "JUICE 10", "WATER 1"]))