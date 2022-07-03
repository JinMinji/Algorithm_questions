def solution(p):
    answer = [0 for i in range(len(p))]

    for i in range(len(p)):
        k = p.index(min(p[i:]))
        if i != k:
            p[i], p[k] = p[k], p[i]
            answer[i] += 1
            answer[k] += 1
        # print(i, p)
    return answer


if __name__ == "__main__":
    print(solution([2, 5, 3, 1, 4]))
    print(solution([2, 3, 4, 5, 6, 1]))
    print(solution([1, 2, 3, 4, 5, 6, 7, 8, 9]))