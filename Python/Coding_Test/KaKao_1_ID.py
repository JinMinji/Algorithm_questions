from string import ascii_lowercase


def solution(new_id):
    # 1단계
    new_id = new_id.lower()

    # 2단계
    right_list = list(ascii_lowercase)
    right_list.extend(['1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '-', '_', '.'])

    listId = list(new_id)

    i = 0
    while i < len(listId):
        if listId[i] not in right_list:
            listId.pop(i)
        else:
            i += 1

    # 3단계
    count = 0
    i = 0
    while i < len(listId):
        if listId[i] == '.':
            count += 1
            if count >= 2:
                listId.pop(i)
                count -= 1
            else:
                i += 1
        else:
            count = 0
            i += 1

    # 4단계 여기서 리스트가 비어있는 경우 처리해야함
    if len(listId) != 0:
        if listId[0] == '.':
            listId.pop(0)

    if len(listId) != 0:
        if listId[-1] == '.':
            listId.pop(-1)

    print(listId)
    # 5단계
    if len(listId) == 0:
        listId.append('a')

    print(listId)

    # 6단계
    if len(listId) >= 16:
        listId = listId[:15]
        if listId[-1] == '.':
            listId.pop(-1)

    # 7단계
    if len(listId) <= 2:
        while len(listId) != 3:
            listId.append(listId[-1])

    answer = listId
    return answer

# print(solution("...!@BaT#*..y.abcdefghijklm"))
# print(solution("z-+.^."))
print(solution("=.="))
print(solution("123_.def"))
print(solution("abcdefghijklmn.p"))
