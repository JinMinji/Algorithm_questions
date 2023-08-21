# 메뉴 리뉴얼
import itertools


def solution(orders, course):
    answer = []

    menu_sets = [{} for i in range(11)]

    for i in range(len(orders)):
        tmp_order_list = list(orders[i])

        tmp_order_list.sort()
        for k in range(2, len(tmp_order_list)+1):
            combs = list(itertools.combinations(tmp_order_list, k))
            for c in combs:
                menu_sets[k][c] = menu_sets[k].get(c, 0) + 1

    for k in course:
        max_cnt = 2
        tmp_ans = []
        for key, val in menu_sets[k].items():
            if val > max_cnt:
                max_cnt = val
                tmp_ans = [key]
            elif val == max_cnt:
                tmp_ans.append(key)

        answer.extend(tmp_ans)

    answer.sort()

    for i in range(len(answer)):
        answer[i] = ''.join(answer[i])

    return answer


if __name__ == '__main__':
    print(solution(["ABCD", "ABCD", "ABCD"], [2,3,4]))