# 양궁
# 완전 냅색같은데 ㅡㅡ

def archery(info, n, score):
    if n == 0 or score == 0:
        return 0

    if info[score] > n:
        return archery(info, n, score-1)
    else:
        return max(score-1 + archery(info, n - (info[score-1]+1), score-1), )


def solution(n, info):
    answer = [-1]   # 이길 방법이 없으면 [-1]

    info.reverse()    # 0점부터 10점 순서로 볼 수 있게 reverse

    # n발을 쏠 수 있고,
    # x 점수를 가져오려면, info[x] + 1 만큼의 화살 수가 필요하다.
    # 격차는 *2,
    # 10점을 어피치가 가져갈 때 어피치 10, 라이언 0 (격차 -10)
    # 라이언이 가져갈 때 어피치 0, 라이언 10 (격차 10)
    # 10점의 *2 만큼 격차 차이가 남



if __name__ == '__main__':
    print(solution(5, [2,1,1,1,0,0,0,0,0,0,0]))