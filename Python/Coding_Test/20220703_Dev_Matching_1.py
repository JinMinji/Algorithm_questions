def solution(grade):
    answer = 0
    # 점수는 증가할 수 없고, 감소할 수만 있다.
    for i in range(len(grade) - 2, -1, -1):
        if grade[i] < grade[i + 1]:
            continue
        else:
            answer += grade[i] - grade[i + 1]
            grade[i] = grade[i + 1]

    return answer


if __name__ == "__main__":
    print(solution([2, 1, 3]))
    print(solution([1, 2, 3]))
    print(solution([3, 2, 3, 6, 4, 5]))