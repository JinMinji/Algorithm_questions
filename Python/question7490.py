# 드디어 해보는 완전탐색.. 이거하고 안랩했으면
# 한문제는 더 풀었겠따!!!

# 연산자 리스트와
# 숫자 리스트를 나눠 생각할 것

import copy
# 재귀함수
def recursive(array, n):
    if len(array) >= n:
        operator_list.append(copy.deepcopy(array)) #deepcopy
        # operator_list.append(array) #deepcopy
        return

    array.append(' ')
    recursive(array, n)
    array.pop()


    array.append('+')
    recursive(array, n)
    array.pop()

    array.append('-')
    recursive(array, n)
    array.pop()

case_num = int(input())

for _ in range(case_num):
    operator_list = []
    n = int(input())
    recursive([], n-1)

    integers = [i for i in range(1, n+1)]

    for operators in operator_list:
        string = ""
        for i in range(n-1):
            string += str(integers[i]) + operators[i]
        string += str(integers[-1])
        if eval(string.replace(" ", "")) == 0:
            print(string)
    print()

