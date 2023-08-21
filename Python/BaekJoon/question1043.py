# 거짓말

people, party = map(int, input().split(" "))


truth = list(map(int, input().split(' ')))

parties = list()

for _ in range(party):
    can = True
    party_mem = list(map(int, input().split(' ')))
    party_mem.pop(0)  # 파티에 몇명오는지는 신경안씀

    parties.append(party_mem)

if truth.pop(0) == 0:    # 0명이 알면 모든 파티 수 리턴
    print(party)
else:
    while len(truth) > 0:
        truth_person = truth.pop(0)
        delete_index = list()
        for i in range(len(parties)):
            if truth_person in parties[i]:
                truth.extend(parties[i])
                tmp_set = set(truth)  # 중복제거
                truth = list(tmp_set)
                delete_index.append(i)
        delete_index.sort(reverse=True)
        for _ in delete_index:
            parties.pop(_)

    result = len(parties)

    print(result)