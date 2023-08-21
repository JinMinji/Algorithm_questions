def make_same1(q1, q2):
    global answer, target

    if answer > (len(q1) + len(q2)):
        # 이건 방법이 없다는 뜻.
        answer = -1
        return

    if sum(q1) > sum(q2):
        # 작은쪽
        mini = q2
        tmp = q1

    else:
        mini = q1
        tmp = q2

    cur = sum(mini)
    for i in range(len(tmp)):
        cur += tmp[i]
        if cur == target:
            answer += i + 1
            return

        if cur > target:
            cur -= tmp[i]
            for j in range(i):
                mini.append(tmp.pop())

            a = tmp.pop()  # i번째 원소
            tmp.append(a)  # 뒤에 붙이기
            make_same(mini, tmp)
            break


def make_same(q1, q2, cnt):
    if cnt > (len(q1) + len(q2)):
        # 이건 방법이 없다는 뜻.
        return -1

    if sum(q1) == sum(q2):
        return cnt

    elif sum(q1) < sum(q2):
        q1.append(q2.pop(0))
        return make_same(q1, q2, cnt + 1)

    else:
        q2.append(q1.pop(0))
        return make_same(q1, q2, cnt + 1)


def solution(queue1, queue2):
    global answer, target
    answer = 0

    # 두 집합의 원소의 합이 같다는 것은
    # 각 집합의 합이, 전체 합 // 2 라는 것.
    # 전체합 // 2 를 만들 수 있는 원소 조합이 2개는 있는지 확인하고
    # 없으면 -1

    target = (sum(queue1) + sum(queue2)) / 2

    # 홀수여도 안됨
    if ((sum(queue1) + sum(queue2)) % 2) != 0:
        return -1

    # 하나의 원소가 이미 target을 넘어서도 안됨
    if max(queue1) > target or max(queue2) > target:
        return -1

    answer = make_same(queue1, queue2, 0)

    return answer