def solution(s):
    int_list = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    answer_string = ''
    for i in range(len(s)):
        if s[i] in int_list:
            answer_string += s[i]
        elif s[i:i + 4] == 'zero':
            answer_string += '0'
        elif s[i:i + 3] == 'one':
            answer_string += '1'
        elif s[i:i + 3] == 'two':
            answer_string += '2'
        elif s[i:i + 5] == 'three':
            answer_string += '3'
        elif s[i:i + 4] == 'four':
            answer_string += '4'
        elif s[i:i + 4] == 'five':
            answer_string += '5'
        elif s[i:i + 3] == 'six':
            answer_string += '6'
        elif s[i:i + 5] == 'seven':
            answer_string += '7'
        elif s[i:i + 5] == 'eight':
            answer_string += '8'
        elif s[i:i + 4] == 'nine':
            answer_string += '9'

    answer = int(answer_string)
    return answer