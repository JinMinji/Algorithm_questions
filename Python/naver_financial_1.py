def solution(id_list, k):
    answer = 0
    coupon = dict()
    for i in range(len(id_list)):
        tmp_list = id_list[i].split()
        tmp_list = set(tmp_list)
        tmp_list = list(tmp_list)   #중복제거
        for j in range(len(tmp_list)):
            coupon[tmp_list[j]] = coupon.get(tmp_list[j], 0) + 1

    for key, value in coupon.items():
        answer += min(k, value)
    return answer


if __name__ == '__main__':
    # print(solution(["A B C D", "A D", "A B D", "B D"], 2))
    print(solution(["JAY", "JAY ELLE JAY MAY", "MAY ELLE MAY", "ELLE MAY", "ELLE ELLE ELLE", "MAY"], 3))

