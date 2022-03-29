def find(word, x, goods):
    for i in range(len(goods)):
        if i != x:
            for w in range(len(goods[i]) - len(word)+1):
                if goods[i][w:w+len(word)] == word:
                    return False
                # for k in range(len(word)):
                #     if goods[i][w + k] == word[k]:
                #         cnt += 1
                #         if cnt == len(word):
                #             return False
                #     else:
                #         cnt = 0
                #         continue

    return True


def solution(goods):
    answer = [[] for i in range(len(goods))]
    for g in range(len(goods)):  # 최대 100개
        res_len = 0
        for i in range(1, len(goods[g])+1):     # 최대 20개
            for j in range(len(goods[g])-i+1):
                target = goods[g][j:j+i]
                if find(target, g, goods):
                    if res_len == 0:
                        res_len = i
                        answer[g].append(target)

                    elif res_len == i:
                        if target not in answer[g]:
                            answer[g].append(target)
                    else:
                        break

    for i in range(len(answer)):
        if not answer[i]:
            answer[i] = "None"
        else:
            answer[i].sort()
            answer[i] = " ".join(answer[i])

    return answer


if __name__ == '__main__':
    # print('2번')
    # input_list = ["pencil","cilicon","contrabase","picturelist"]
    # print(solution(input_list))

    print()
    print('1번')
    input_list = ["abcdeabcd","cdabe","abce","bcdeab"]
    print(solution(input_list))