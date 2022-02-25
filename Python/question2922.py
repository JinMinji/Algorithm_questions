#20210825 즐거운 단어

consonants = ['A', 'E', 'I', 'O', 'U']
# 모음은 5개
# 자음은 21개
# 밑줄은 최대 10개


def find_ways(word, index, c_cnt, v_cnt, l_cnt, res):
    global result
    if index == len(word):
        if l_cnt > 0:
            result += res
        return
    if word[index] == '_':
        if c_cnt < 2:
            find_ways(word, index+1, c_cnt+1, 0, l_cnt, res*5)
        if v_cnt < 2:
            find_ways(word, index+1, 0, v_cnt+1, l_cnt, res*20)
            find_ways(word, index+1, 0, v_cnt+1, l_cnt+1, res)

    elif word[index] in consonants:
        c_cnt += 1
        if c_cnt == 3:
            return
        find_ways(word, index + 1, c_cnt, 0, l_cnt, res)

    else:
        v_cnt += 1
        if word[index] == 'L':
            l_cnt += 1
        if v_cnt == 3:
            return

        find_ways(word, index + 1, 0, v_cnt, l_cnt, res)


if __name__ == '__main__':
    global result

    result = 0

    word = input()

    find_ways(word, 0, 0, 0, 0, 1)

    print(result)

