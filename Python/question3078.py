# 좋은 친구 골드 3


if __name__ == '__main__':
    N, K = map(int, input().split(' '))

    name_list = [[] for i in range(21)]  # 이름 글자수 최대 20자.

    result = 0

    for i in range(K+1):
        student = input()
        result += len(name_list[len(student)])
        name_list[len(student)].append(i)

    for i in range(K+1, N):
        student = input()
        n = len(student)
        in_idx = -1
        for _ in range(len(name_list[n])):
            if name_list[n][_] >= i-K:
                in_idx = _
                break
        if in_idx == -1:
            name_list[n] = []
        else:
            name_list[n] = name_list[n][in_idx:]
        result += len(name_list[n])
        name_list[len(student)].append(i)

    print(result)