import sys

sys.setrecursionlimit(10 ** 7)

from collections import deque


def make_same(q1, q2, sum1, target, cnt):
    if cnt > 2 * (len(q1) + len(q2)):
        # 이건 방법이 없다는 뜻.
        return -1

    if sum1 == target:
        return cnt

    elif sum1 < target:
        tmp = q2.popleft()
        sum1 += tmp
        q1.append(tmp)
        return make_same(q1, q2, sum1, target, cnt + 1)

    else:
        # q2.append(q1.pop(0))
        tmp = q1.popleft()
        sum1 -= tmp
        q2.append(tmp)
        return make_same(q1, q2, sum1, target, cnt + 1)


def solution(queue1, queue2):
    # 두 집합의 원소의 합이 같다는 것은
    # 각 집합의 합이, 전체 합 // 2 라는 것.

    target = (sum(queue1) + sum(queue2)) // 2

    # 홀수여도 안됨
    if ((sum(queue1) + sum(queue2)) % 2) != 0:
        return -1

    # 하나의 원소가 이미 target을 넘어서도 안됨
    if (max(queue1) > target) or (max(queue2) > target):
        return -1

    deq1 = deque(queue1)
    deq2 = deque(queue2)

    answer = make_same(deq1, deq2, sum(queue1), target, 0)

    return answer


if __name__ == "__main__":
    print(solution([3, 2, 7, 2], [4, 6, 5, 1]))
    print(solution([1, 2, 1, 2], [1, 10, 1, 2]))