def solution(s):
    answer = len(s)

    for k in range(1, len(s)):  # k개 단위로 잘라서 압축하기
        pre = 0
        cnt = 1
        res = ''
        for i in range(1, len(s) // k + 1):
            now = i * k
            if s[pre:now] == s[now:now + k]:
                cnt += 1
            else:
                if cnt > 1:
                    res += str(cnt)
                res += s[pre:now]
                cnt = 1
            pre = now

        if cnt == 1:
            res += s[pre:now]

        res += s[pre:]

        if answer > len(res):
            answer = len(res)

    return answer


if __name__ == '__main__':
    print(solution("ababcdcdababcdcd"))