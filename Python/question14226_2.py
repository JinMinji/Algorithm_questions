# 20210728 이모티콘 두번째 풀이
from collections import deque


def min_making_time(n):
    to_visit = deque()
    to_visit.append([1, 0])

    while to_visit:
        text, clipbloard = to_visit.popleft()
        if text == n:
            print(dp_con[text][clipbloard])
            break

        # 복사
        if dp_con[text][text] == -1:
            dp_con[text][text] = dp_con[text][clipbloard] + 1
            to_visit.append([text, text])

        # 붙여넣기
        if dp_con[text+clipbloard][clipbloard] == -1:
            dp_con[text+clipbloard][clipbloard] = dp_con[text][clipbloard] + 1
            to_visit.append([text+clipbloard, clipbloard])

        # 삭제
        if dp_con[text-1][clipbloard] == -1:
            dp_con[text-1][clipbloard] = dp_con[text][clipbloard] + 1
            to_visit.append([text-1, clipbloard])


if __name__ == '__main__':
    N = int(input())

    dp_con = [[-1 for i in range(5000)] for i in range(5000)]
    dp_con[1][0] = 0
    min_making_time(N)
