def solution1(S):
    # write your code in Python 3.6
    count = 0
    answer = 0
    for i in S:
        if i != 'a':
            if count == 0:
                answer += 2
            elif count == 1:
                answer += 1
                count = 0
            else:
                count = 0
        else:
            count += 1
            if count >= 3:
                return -1

    if S[-1] != 'a':
        answer += 2

    return answer


def solution2(S):
    # write your code in Python 3.6
    for i in range(len(S)):
        for j in range(len(S[0])):  # max 2000
            val = S[i][j]
            for k in range(i + 1, len(S)):
                if val == S[k][j]:
                    return [i, k, j]

    answer = -1

    return answer


def solution3(A):
    # write your code in Python 3.6
    result_list = [0 for i in range(len(A))]

    for i in A:
        result_list[i-1] += 1

    print(result_list)
    answer = 0
    for i in range(len(result_list)):
        while result_list[i] > 1:
            p = 0
            for j in range(p, len(result_list)):
                if result_list[j] == 0:
                    result_list[j] = 1
                    result_list[i] -= 1
                    answer += abs(i-j)
                    print(i, j)
                    p = j
                    if answer >= 1000000000:
                        return -1
                    break
    print(result_list)
    return answer

# print(solution1('Minji'))
# print(solution2(['Minji', 'kikkk']))
# print(solution2(['jb','bj','kk']))
print(solution3([7,3,4,6,7,4,4]))

def solution(A):
    # write your code in Python 3.6
    result_list = [0 for i in range(len(A))]

    for i in A:
        result_list[i-1] += 1

    answer = 0
    for i in range(len(result_list)):
        if result_list[i] > 1:
            change = 1
            while result_list[i] != 1:
                tmp_i = i - change
                if tmp_i >= 0 and result_list[tmp_i] == 0:
                    result_list[tmp_i] = 1
                    result_list[i] -= 1
                    answer += change
                    if answer >= 1000000000:
                        return -1

                tmp_i = i + change
                if tmp_i < len(result_list) and result_list[tmp_i] == 0:
                    result_list[tmp_i] = 1
                    result_list[i] -= 1
                    answer += change
                    if answer >= 1000000000:
                        return -1

                change += 1

    return answer