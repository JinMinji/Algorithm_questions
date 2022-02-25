def solution(s):
    pre = s[0]
    cnt = 1
    answer = []
    for i in range(1, len(s)):
        if s[i] == pre:
            cnt += 1

        else:
            answer.append(cnt)
            cnt = 1
            pre = s[i]

        if i == len(s) - 1:  # 마지막 이면!
            answer.append(cnt)

    if s[0] == pre:  # 첫번째 글자와 마지막 글자가 같으면,
        tmp = answer.pop()
        answer[0] += tmp

    answer.sort()

    return answer