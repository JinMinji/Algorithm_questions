# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(S):
    # write your code in Python 3.6
    flag = True
    if S[0] == 'b':
        flag = False

    answer = True
    for i in range(1, len(S)):
        if S[i] == 'a':
            if not flag:
                answer = False
                break
        else:
            flag = False

    return answer
