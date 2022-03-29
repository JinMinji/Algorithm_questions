def solve(cur_state, idx, choice):
    global answer, check, limit

    if idx == len(check):
        answer = max(answer, cur_state[2])
        return

    if choice:
        # alphabet
        for i in range(26):
            if check[idx][0][i] == 1:
                cur_state[0][i] = 1

        # shift
        if check[idx][1]:
            cur_state[1] = True

        need = sum(cur_state[0])
        if cur_state[1]:
            need += 1

        if need > limit:
            return  # 선택 불가 => 더이상 탐색할 필요 없음

        cur_state[2] += check[idx][2]

    solve(cur_state, idx + 1, True)
    solve(cur_state, idx + 1, False)


def solution(sentences, n):
    global answer, check, limit

    limit = n

    answer = -1
    # sentences의 최대 길이가 15이므로, 문자열을 선택할 때, 선택하지 않을 때 2가지 경우를 모두 고려해도
    # 2**15 번의 연산으로 끝남.

    check = [[] for i in range(len(sentences))]

    for i in range(len(sentences)):
        alpha = [0 for i in range(26)]
        shift = False
        cur_word_score = len(sentences[i])

        for j in range(len(sentences[i])):
            if sentences[i][j] == ' ':  # 스페이스바는 패스
                continue

            tmp_ord = ord(sentences[i][j]) - 65  # 대문자 아스키코드
            if tmp_ord < 26:
                cur_word_score += 1  # 대문자는 1점 추가
                alpha[tmp_ord] = 1
                shift = True  # 대문자 shift

            else:
                tmp_ord -= 32
                alpha[tmp_ord] = 1

        need = sum(alpha)
        if shift:
            need += 1

        if need > n:
            cur_word_score = 0

        check[i] = [alpha, shift, cur_word_score]

    start_state = [[0 for i in range(26)], False, 0]  # alpha, shift, 현재 점수
    solve(start_state, 0, True)  # 선택 할때,
    solve(start_state, 0, False)  # 선택하지 않을 때

    return answer


if __name__ == '__main__':
    print(solution(["line in line", "LINE", "in lion"], 5))
    print(solution(["ABcD", "bdbc", "a", "Line neWs"], 7))