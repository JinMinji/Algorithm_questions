from itertools import combinations

def solution(relation):
    all_comset = list()
    for student in relation:
        comset = list()
        for i in range(len(student)):
            k = list(combinations(student, i+1))
            comset.append(k)

        all_comset.append(comset)

    # all_comset의 첫번째인덱스(=all_comset[0])에는 첫번째 학생의 개수별 속성조합리스트가 들어있다. 속성이 4개면 인덱스도 0~3
    # all_comset[0]의 첫번째인덱스(=all_comset[0][0])에는 첫번째 학생의 1개짜리 속성조합이 담겨있다. [(속성1,),(속성2,),(속성3),(속성4,)]
    # all_comset[0][0]의 첫번째 인덱스(=all_comset[0][0][0])는 첫번째 학생의 1개짜리 첫번째 속성조합이다.


    print(all_comset, len(all_comset), "= 입력 학생수")
    print(all_comset[0], len(all_comset[0]), "= 속성개수")
    print(all_comset[0][0], len(all_comset[0][0]), "= 속성개수")

    attribute_num = len(all_comset[0])

    uniqueness = list()

    for std in all_comset:
        for att_num in range(attribute_num):
            uniqueness.append([])
            print(uniqueness)
            for i in range(len(std[att_num])):
                if len(uniqueness[att_num]) < i+1:
                    uniqueness[att_num].append([])
                uniqueness[att_num][i].append(std[att_num][i])
                print("this", uniqueness[att_num][i])

    return



print(solution([["100","ryan","music","2"],["200","apeach","math","2"],["300","tube","computer","3"],["400","con","computer","4"],["500","muzi","music","3"],["600","apeach","music","2"]]))