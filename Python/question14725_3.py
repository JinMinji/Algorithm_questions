#20210721 개미굴 세번째 풀이

if __name__ == '__main__':
    N = int(input())

    informations = list()
    for i in range(N):
        info = list(map(str, input().split()))
        info.pop(0)    # 맨앞에 개수는 빼준다
        informations.append(info)

    informations.sort() #출력 순서 지정

    for j in range(len(informations[0])):
        print('--'*j+informations[0][j])

    for i in range(1, len(informations)):
        j = 0
        while j <= len(informations[i]):
            if informations[i-1][j] == informations[i][j]:
                j += 1
            else:
                for _ in range(j, len(informations[i])):
                    print('--'*_+informations[i][_])

                break