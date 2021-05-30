#20210524 수 묶기

def max_total():    # 최대합 구하기
    total = 0
    tp = 0
    cnt = 0
    for i in range(0,len(num_list)-1,2):
        if num_list[i] <= 0: # 음수면, 음수끼리 곱하거나 0을 곱해서 -를 없애주는게 좋다!
            if num_list[i+1] <= 0:
                total += num_list[i]*num_list[i+1]
                cnt += 2
                tp = i + 2
            else:
                total += num_list[i]
                tp = i+1
                cnt += 1
                break
        else:
            tp = i
            break
    if cnt < len(num_list[:tp]):
        total += num_list[cnt]
    cnt = 0

    for i in range(tp, len(num_list), 1):       # 1은 곱셈으로 묶지않고, 그냥 더해주는 게 이득.
        if num_list[tp] == 1:
            total += 1
            cnt += 1
            if (tp+1) < len(num_list):
                tp += 1
        else:
            break

    for i in range(len(num_list)-1, tp,-2):
        total += num_list[i]*num_list[i-1]
        cnt += 2
    if cnt != 0 and cnt <= len(num_list[tp:]):
        total += num_list[tp]

    return total

if __name__ == '__main__':
    N = int(input())
    num_list = list()
    for _ in range(N):
        num_list.append(int(input()))

    num_list.sort()

    print(max_total())