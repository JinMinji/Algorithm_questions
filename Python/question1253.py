# 1253, 좋다, 골드4
import sys


def find(num):
    global sum_lst

    start = 0
    end = len(sum_lst)-1
    # res = 0

    while start <= end:
        mid = (start + end)//2
        if sum_lst[mid] < num:
            start = mid + 1
            # res = mid
        elif sum_lst[mid] == num:
            return True
        else:
            end = mid - 1

    return False


if __name__ == "__main__":
    N = int(input())
    num_lst = list(map(int, sys.stdin.readline().split()))
    num_lst.sort()

    sum_lst = list()
    # 0 + 나 = 나 : 0의 개수만큼 빼야된다.
    # 나 + 나 = 나 : 0 + 0 / (0의 개수 * 0의 개수-1)//2 0이 2개면 0개 3개면 그때부터는 다 count!
    # 다른 수 + 다른 수 = 그냥 세준다.

    zero_cnt = 0
    for i in range(N):
        if num_lst[i] == 0: # 0이면 연산 안해줄 거.
            zero_cnt += 1
            continue
        for j in range(i+1, N):
            if num_lst[j] == 0:
                continue
            sum_lst.append(num_lst[i]+num_lst[j])

    sum_lst.sort()

    answer = 0
    cnt = 1
    for i in range(1, N):
        if num_lst[i-1] == num_lst[i]:
            cnt += 1
        else:
            if find(num_lst[i-1]):    # 0을 제외하고도 연산 결과에 있다는 거니까! 이미 좋은 수!
                answer += cnt
            elif zero_cnt > 0 and num_lst[i-1] != 0:  # 0을 제외하면 없지만, 0을 포함 하여 결과가 있을 때!
                if cnt >= 2:
                    answer += cnt
            cnt = 1

    # print(answer)
    # 맨 마지막 체크하기.
    if find(num_lst[-1]):    # 0을 제외하고도 연산 결과에 있다는 거니까! 이미 좋은 수!
        answer += cnt
    elif zero_cnt > 0 and num_lst[-1] != 0: # 0을 제외하면 없지만, 0을 포함 하여 결과가 있을 때!
        if cnt >= 2:
            answer += cnt

    # print(answer)
    if zero_cnt > 2 and 0 not in sum_lst:
        answer += zero_cnt
    print(answer)