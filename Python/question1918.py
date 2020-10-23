#20210511 후위표기식

input_string = input()

# stack 쓰기
operators = list()

result = ''

for c in input_string:
    if c in ['*','/']:
        while(len(operators) > 0 and operators[-1] in ['*','/']):
            result += operators.pop(-1)
        operators.append(c)
    elif c in ['+','-']:
        while(len(operators) > 0 and operators[-1] in ['+','-','*','/']):
            result += operators.pop(-1)
        operators.append(c)
    elif c == '(':
        operators.append(c)
    elif c == ')':
        while operators[-1] != '(':
            result += operators.pop(-1)
        operators.pop(-1)
    else:
        result += c

while len(operators) > 0:
    result += operators.pop(-1)

print(result)