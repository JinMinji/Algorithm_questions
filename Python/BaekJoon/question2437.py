# 저울
# 누적합을 모르면 그냥 절대 풀 수 없는 문제

if __name__ == '__main__':
    N = int(input())

    w_list = list(map(int, input().split(' ')))
    w_list.sort()

    result = sum(w_list)+1

    # 작은 수부터 누적합 확인

    if 1 not in w_list:
        print(1)
    else:
        cur_total = 0
        for i in range(len(w_list)):
            # 현재까지의 누적합보다 2이상 큰 수가 다음으로 나오면,
            # 현재까지의 누적합 +1 의 수를 만들 수 없음을 이용.
            if cur_total + 1 < w_list[i]:
                break

            else:
                cur_total += w_list[i]

        print(cur_total + 1)

