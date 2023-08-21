#프로그래머스 하계인턴 코딩챌린지

#문제1
#
def solution(atmos):
    answer = 0

    mask = False
    cur_day = 0
    for i in range(len(atmos)):
        if atmos[i][0] > 80 or atmos[i][1] > 35:
            #마스크 껴야하는 날.
            if mask:    #끼던 마스크가 있을 때
                cur_day += 1
                if cur_day > 2:
                    cur_day = 0
                    answer += 1

            else:   #끼던 마스크가 없을 때
                mask = True
                answer += 1
                cur_day = 0

            if atmos[i][0] > 150 and atmos[i][1] > 75:
                #사용하고 바로 폐기 해야 하는날
                cur_day = 2




        else: #안껴도 되는 날.
            if mask:
                cur_day += 1
                if cur_day > 2:
                    mask = False
                    cur_day = 0

    return answer