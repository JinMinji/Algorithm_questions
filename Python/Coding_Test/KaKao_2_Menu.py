from itertools import combinations

def solution(orders, course):
    order_dic = dict()
    for i in course: # 개수 별
        for j in orders:
            if i not in order_dic:
                order_dic[i] = list(combinations(j, i))
            else:
                order_dic[i] = order_dic[i]+list(combinations(j, i))
    print(order_dic[2][1])

    for num in course:
        for i in range(len(order_dic[num])):
            lst = list(order_dic[num][i])
            lst.sort()
            order_dic[num][i] = ''.join(lst)


    # 모든 메뉴의 개수별 조합을 중복없이 담은 list = order_dic
    max_set = dict()
    # 각 개수별 최다주문 조합을 넣을 딕셔너리

    for i in order_dic:
        num_set = []
        for k in order_dic[i]:
            if order_dic[i].count(k)>= 2:
                num_set.append(k)

        max_cnt = 2
        if len(num_set) != 0:
            max_set[i] = num_set[0]
            for k in num_set:
                cnt = num_set.count(k)
                if cnt > max_cnt:
                    max_cnt = cnt
                    max_set[i] = k
                if cnt == max_cnt:
                    if k not in max_set[i]:
                        max_set[i] += " " + k
                    # print(cnt, max_set[i], k)
    answer = []
    for i in max_set.values():
        lst = i.split()
        for j in lst:
            answer.append(j)

    answer.sort()

    return answer


print(solution(["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"],[2,3,4]))
print(solution(["ABCDE", "AB", "CD", "ADE", "XYZ", "XYZ", "ACD"],[2,3,5]))
print(solution(["XYZ", "XWY", "WXA"],[2,3,4]))


#
    # for num in course: # 메뉴개수별로 확인한다.
    #     max_value = 2 # 주문 최댓값을 담을 변수 # 최소 2번의 주문은 들어와야함.
    #     max_set[num] = [-1]
    #     for i in order_dic[num]: # 현재 개수(num)별 조합이 담긴 리스트의 아이템
    #         count = order_dic[num].count(i)
    #         if count == max_value: # 동일한 경우에는 추가해주고
    #             if max_set[num] == -1:
    #                 max_set[num] = [i]
    #                 max_value = count
    #             else:
    #                 max_set[num] = max_set[num].append(i)
    #                 print(max_set)
    #         elif count > max_value: # 더 큰 경우에는 바꿔준다.
    #             max_set[num] = [i]
    #             max_value = count
    #
    # for y in max_set.values():
    #     set_menu.append(y)
