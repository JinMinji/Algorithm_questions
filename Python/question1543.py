string = input()
search_str = input()

count = 0
bp = 0 # backup point
j = 0
i = 0

while i < len(string):
    if string[i] == search_str[j]:
        if j == len(search_str)-1:
            count += 1
            j = 0
        else : j += 1
    else :
        i = i-j
        j = 0
    i += 1

print(count)
