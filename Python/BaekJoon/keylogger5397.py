casenum = int(input())

for i in range(casenum):
    keylog = input()
    password = []
    cursor = -1

    for k in keylog:
        if k == '-':
            if cursor > -1:
                password.pop(cursor)  #스택에서 내보낸다.
                cursor -= 1

        elif k == '<':
            if cursor > -1:
                cursor -= 1

        elif k == '>':
            if cursor < len(password) -1:
                cursor += 1

        else:
            password.insert(cursor+1, k)
            cursor += 1

    print(''.join(password))

    #문제에서 요구하는 대로 그냥 쓰면, 데이터가 너무 많기때문에 해결되지않음.
    #선형시간 안에 해결할 수 있는, 알고리즘을 적절히 이용해야하는 문제.
