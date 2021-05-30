#20210525 수 묶기

def max_total():    # 최대합 구하기
    total = 0

    # 1. 음수이거나, 0 일 때 : 짝수개면 작은 수끼리 곱하고, 홀수개면 제일 큰 수(절대값은 제일 작은 수)를 남겨서 더한다.
    tp = 0 # 음수, 양수를 나누기 위한 인덱스값 변수
    for i in range(len(num_list)):
        if num_list[i] > 0:
            tp = i
            break

    n_num = num_list[:tp]    # 음수만 담긴 리스트 (0도 포함)
    p_num = num_list[tp:]    # 양수만 담긴 리스트

    for i in range(len(n_num)//2):
        total += (n_num[2*i])*(n_num[2*i+1])
    if len(n_num) % 2 != 0:  # 홀수 개면,
        total += n_num[-1]

    tp = tp
    for i in range(len(p_num)):
        if p_num[i] == 1:
            total += 1
            tp += 1
        else:
            break

    p_num = num_list[tp:]

    p_num.sort(reverse=True)
    for i in range(len(p_num) // 2):
        total += (p_num[2 * i]) * (p_num[2 * i + 1])
    if len(p_num) % 2 != 0:  # 홀수 개면,
        total += p_num[-1]

    return total

if __name__ == '__main__':
    N = int(input())
    global num_list
    num_list = list()
    for _ in range(N):
        num_list.append(int(input()))

    num_list.sort()

    print(max_total())