#프로그래머스 하계인턴 코딩챌린지

#문제2

def solution(rooms, target):
    answer = []
    member = dict()

    for i in range(len(rooms)):
        num, names = rooms[i].split("]")
        num = int(num[1:])
        names = names.split(",")
        for n in names:
            member[n] = member.get(n, [])
            member[n].append(num)

    # print(member)

    tmp_res = list()

    for mem, nums in member.items():
        tmp_prior = 10000
        for n in nums:
            tmp_prior = min(tmp_prior, abs(target - n))

        if tmp_prior != 0:
            tmp_res.append([len(nums), tmp_prior, mem])

    tmp_res.sort(key=lambda x: (x[0], x[1], x[2]))

    for r in tmp_res:
        answer.append(r[2])

    return answer


if __name__ == "__main__":
    solution(["[403]James", "[404]Azad,Louis,Andy", "[101]Azad,Guard"], 403)