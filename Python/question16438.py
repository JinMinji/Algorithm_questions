# 20210706 원숭이 스포츠

a = 'A'
b = 'B'


def dp_made(n):
    result = list()
    if n % 2 == 0:  # 짝수
        h = n // 2
        tmp_list = dp(h)
        for i in range(len(tmp_list)):
            tmp_list[i].extend(tmp_list[i])
            result.append(tmp_list[i])

        tmp = [a for i in range(h)]
        tmp.extend([b for i in range(h)])
        result.append(tmp)

    else:
        h = n // 2
        tmp_list1 = dp(h)
        tmp_list2 = dp(h + 1)
        for i in range(len(tmp_list1)):
            tmp_list1[i].extend(tmp_list2[i])
            result.append(tmp_list1[i])

        if len(tmp_list1) != len(tmp_list2):
            tmp_list1[i].extend(tmp_list2[i])
            result.append(tmp_list1[i])

        tmp = [a for i in range(h)]
        tmp.extend([b for i in range(h + 1)])
        result.append(tmp)

    dp_dic[n] = result

    return result


def dp(n):
    if not dp_dic.get(n, []):  # 구해놓은 dp가 없으면!
        if n == 1:
            dp_dic[n] = [[a]]

        elif n == 2:
            dp_dic[n] = [[a, b]]

        else:
            dp_dic[n] = dp_made(n)

    return dp_dic[n]


if __name__ == '__main__':
    N = int(input())
    dp_dic = dict()
    answer = dp(N)
    # print(answer)
    for i in range(7):
        print(answer[i % len(answer)])