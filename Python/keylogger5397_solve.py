casenum = int(input())

for _ in range(casenum) :
    keylog = input()
    left_stack = []
    right_stack = []

    for i in keylog:
        if i == '-':
            if left_stack:
                left_stack.pop()
        elif i == '<':
            if left_stack:
                right_stack.append(left_stack.pop())
        elif i == '>':
            if right_stack:
                left_stack.append(right_stack.pop())
        else:
            left_stack.append(i)
    left_stack.extend(reversed(right_stack))
    print(''.join(left_stack))


#와우.. 시간초과.. 그런 것도 고려할것!!