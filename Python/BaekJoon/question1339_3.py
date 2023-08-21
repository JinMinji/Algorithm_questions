# 단어 수학

def string_cal(match_list, string_list):
    result = 0

    for s in string_list:
        tmp_s = ''
        for i in range(len(s)):
            tmp_s += str(match_list[ord(s[i])-65])

        result += int(tmp_s)

    return result


if __name__ == '__main__':
    N = int(input())

    # 알파벳(아스키코드 - 65, 0이 A) x가 n자릿수에 몇개 있는지 => alphabet[x][n]
    alphabet = [[0 for i in range(8)] for i in range(26)]

    input_list = list()

    for _ in range(N):
        word = input()
        input_list.append(word)

        for i in range(len(word)):
            c = ord(word[i]) - 65  # 알파벳 아스키코드
            alphabet[c][len(word) - i] += 1

    num_match = [-1 for i in range(26)]

    cur = 9

    for k in range(7, -1, -1):
        max_val = -1
        next_list = list()
        for a in range(len(alphabet)):
            if alphabet[a][k] != 0 and num_match[a] == -1:
                if max_val == -1:
                    max_val = a
                else:
                    next_list.append(a)
                    for j in range(7, -1, -1):
                        if alphabet[a][j] > alphabet[max_val][j]:
                            next_list.pop()
                            next_list.append(max_val)
                            max_val = a
                            break

                        elif alphabet[a][j] < alphabet[max_val][j]:
                            break

        if max_val != -1:
            num_match[max_val] = cur
            cur -= 1

        if next_list:
            for n in next_list:
                num_match[n] = cur
                cur -= 1

    print(string_cal(num_match, input_list))



