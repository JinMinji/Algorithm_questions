
def check_right(s):
    stack_lst = list()
    isRight = True

    for i in range(len(s)):
        if s[i] == '(':
            stack_lst.append('(')
        else:
            if stack_lst and stack_lst[-1] == '(':
                stack_lst.pop()

            else:
                isRight = False
                return isRight

    return isRight


def divide(u, v):
    open_cnt = 0
    close_cnt = 0

    for i in range(len(v)):
        if v[i] == '(':
            open_cnt += 1

        else:  # (와 )로만 이뤄져있음
            close_cnt += 1

        if open_cnt == close_cnt:  # 최단길이의 균형잡힌 괄호문자열 : u
            if check_right(v[:i + 1]):  # 올바른 괄호문자열이면
                u += v[:i + 1]
                v = v[i+1:]         # 남은문자열 v
                u += divide('', v)  # 에 대해 수행한 결과를 붙인다.
                return u

            else:   # 올바른 괄호문자열이 아니라면,
                u = v[:i + 1]
                tmp_res = '('   # ( + v수행결과 + ) + u 앞뒤자르고 괄호방향 뒤집은것
                tmp_res += divide('', v[i+1:])
                tmp_res += ')'
                tmp_u = ''
                if len(u) > 2:
                    u = u[1:-1]
                    for k in range(len(u)):
                        if u[k] == '(':     # 방향 뒤집기
                            tmp_u += ')'
                        else:
                            tmp_u += '('

                tmp_res += tmp_u

                return tmp_res

    return u    # 빈 문자열일 때, 빈문자열 반환


def solution(p):
    answer = divide('', p)

    return answer


if __name__ == '__main__':
    print(solution("()))((()"))