# 단어 수학

def string_cal(match_dict, str_list):
    result = 0

    for s in str_list:
        tmp_s = ''
        for i in range(len(s)):
            tmp_s += str(match_dict[ord(s[i])-65])

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
            alphabet[c][8-len(word) + i] += 1

    tmp_match = []

    for w in range(len(alphabet)):
        check_num = int(''.join([str(int) for int in alphabet[w]]))
        if check_num > 0:
            tmp_match.append([check_num, w])

    tmp_match.sort(key=lambda x: x[0], reverse=True)

    num_match = dict()
    cur = 9

    for i in range(len(tmp_match)):
        num_match[tmp_match[i][1]] = cur
        cur -= 1

    print(string_cal(num_match, input_list))



