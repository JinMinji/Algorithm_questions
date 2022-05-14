def solution(survey, choices):
    answer = ''

    type_cnt = dict()
    type_cnt["R"] = 0
    type_cnt["T"] = 0

    type_cnt["C"] = 0
    type_cnt["F"] = 0

    type_cnt["J"] = 0
    type_cnt["M"] = 0

    type_cnt["A"] = 0
    type_cnt["N"] = 0


    for i in range(len(survey)):
        if choices[i] < 4:
            # 동의쪽
            type_cnt[survey[i][0]] += (4-choices[i])

        elif choices[i] == 4:
            # 어느 쪽에도 점수를 더하지 않음.
            continue

        else:   #( choices[i] > 7)
            # 비동의쪽
            type_cnt[survey[i][1]] += (choices[i] - 4)

    if type_cnt["R"] >= type_cnt["T"]:
        answer += "R"
    else:
        answer += "T"

    if type_cnt["C"] >= type_cnt["F"]:
        answer += "C"
    else:
        answer += "F"

    if type_cnt["J"] >= type_cnt["M"]:
        answer += "J"
    else:
        answer += "M"

    if type_cnt["A"] >= type_cnt["N"]:
        answer += "A"
    else:
        answer += "N"

    return answer