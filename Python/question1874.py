# 백준1874
# stack 문제 난이도 : 하
# 제한시간 30분

n = int(input("입력하세요 : "))

numlist = [] #입력숫자들을 담을 리스트
for i in range(0, n):
    k = int(input())
    numlist.append(k)

input_list = []
for i in range(n, 0,-1):
    input_list.append(i)

stack = [] # +-연산에 사용할 스택
result = [] # +-결과값을 담을 리스트
# 처음 시작할 때는, 맨처음 입력값(numlist[0])이 나올때까지 더해준다.
# 스택에도 오름차순으로 값을 담아준다.

for num in numlist:
    if not stack:  #스택이 비어 있으면,
        stack.append(input_list.pop())
        result.append('+')

    if num > stack[-1]:
        while num > stack[-1]:
            stack.append(input_list.pop())
            result.append('+')
        stack.pop()
        result.append('-')

    elif num == stack[-1]:
        stack.pop()
        result.append('-')

    elif num < stack[-1]:
        result = []
        break

if not result:
    print("NO")

else:
    for value in result:
        print(value)
