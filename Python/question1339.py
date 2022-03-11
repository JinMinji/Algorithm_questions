#단어 수학


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

    # 숫자 최대길이는 8,
    # 각 자릿수에 어떤 알파벳이 가장 많은지 체크.
    # 제일 큰 자릿수에 많은 애부터 높은 수를 차례로 매칭해주면 됨
    max_list = [[] for _ in range(8)]
    check = [0 for i in range(26)]
    # 자릿수가 큰 것부터 인덱스 0에서 시작.

    for k in range(8):
        cur_max = 0
        for i in range(len(alphabet)):
            if check[i] == 0:
                check[i] = 1
                if alphabet[i][7-k] != 0 and alphabet[i][7-k] == cur_max:
                    max_list[k].append(i)

                elif alphabet[i][7-k] > cur_max:
                    max_list[k] = [i]

    # print(alphabet)
    print(max_list)

    match_list = [-1 for i in range(10)]

    result = 0

    # for i in range(max_list):




