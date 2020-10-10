
def count_num(arr):
    total = 0
    for row in arr:
        for i in row:
            total += i

    if total == 0:  # 다 0이라는 의미
        answer[0] += 1

    elif total == len(arr)**2 :  # 다 1이라는 의미
        answer[1] += 1

    else:
        quad1 = []
        quad2 = []
        quad3 = []
        quad4 = []
        mid = len(arr)//2
        for i in range(mid):
            quad1.append(arr[i][:mid])
            quad2.append(arr[i][mid:])

        for i in range(mid, len(arr)):
            quad3.append(arr[i][:mid])
            quad4.append(arr[i][mid:])

        count_num(quad1)
        count_num(quad2)
        count_num(quad3)
        count_num(quad4)

def solution(arr):
    global answer
    answer = [0, 0]

    count_num(arr)

    return answer


solution([[1,1,0,0],[1,0,0,0],[1,0,0,1],[1,1,1,1]])

