def solution(arr):
    answer = []
    cnt_lst = [0, 0, 0]  # 1, 2, 3의 개수
    for i in range(len(arr)):
        cnt_lst[arr[i] - 1] += 1

    max_cnt = max(cnt_lst)
    for cnt in cnt_lst:
        answer.append(max_cnt - cnt)

    return answer