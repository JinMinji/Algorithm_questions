#프로그래머스 하계인턴 코딩챌린지

#문제3

def solution(line):
    answer = []

    # 현재 손가락 위치
    left = [1, 0]
    right = [1, 9]

    left_lst = ['1', '2', '3', '4', '5', 'Q', 'W', 'E', 'R', 'T']
    right_lst = ['6', '7', '8', '9', '0', 'Y', 'U', 'I', 'O', 'P']
    num_key = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
    char_key = ['Q', 'W', 'E', 'R', 'T', 'Y', 'U', 'I', 'O', 'P']

    for c in line:
        target = [-1, -1]
        if c in num_key:
            target = [0, num_key.index(c)]
        else:
            target = [1, char_key.index(c)]

        left_dist = abs(left[0] - target[0]) + abs(left[1] - target[1])
        right_dist = abs(right[0] - target[0]) + abs(right[1] - target[1])

        if left_dist == right_dist:
            #맨하탄거리가 같으면,
            if abs(left[1] - target[1]) == abs(right[1] - target[1]):
                #수평거리도 같으면
                if c in left_lst:
                    # 어느쪽 자판에 포함인지 확인
                    answer.append(0)
                    left[0] = target[0]
                    left[1] = target[1]
                else:
                    answer.append(1)
                    right[0] = target[0]
                    right[1] = target[1]

            elif abs(left[1] - target[1]) < abs(right[1] - target[1]):
                answer.append(0)
                left[0] = target[0]
                left[1] = target[1]
            else:
                answer.append(1)
                right[0] = target[0]
                right[1] = target[1]

        elif left_dist < right_dist:
            answer.append(0)
            left[0] = target[0]
            left[1] = target[1]

        else:
            answer.append(1)
            right[0] = target[0]
            right[1] = target[1]

    return answer


if __name__ == "__main__":
    print(solution("64E2"))