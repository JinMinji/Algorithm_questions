#백준 알고리즘 1966

# 중요도 - 프린터

#입력 형식

def findmax(list):
    max_value = list[0][1]
    max_i = 0
    for i in range(len(list)):
        if list[i][1] > max_value:
            max_value = list[i][1]
            max_i = i
    return max_i

casenum = int(input()) #테스트 케이스의 개수
result = []

for i in range(0, casenum):
    n, m = map(int, input().split(' '))
    importance = list(map(int, input().split(' ')))

    document = []
    for i in range(0, len(importance)):
        document.append([i, importance[i]])

    rank = 0
    # 두번째 도전

    while True:
        if document[0][1] == document[findmax(document)][1]:
            rank += 1
            if document[findmax(document)][0] == m:
                result.append(rank)
                break
            else:
                document.pop(0)
        else:
            document.append(document.pop(0))

for value in result:
    print(value)
