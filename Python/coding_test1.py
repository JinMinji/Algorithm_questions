def factorial(n):
    fac_list = list()
    for i in range(n + 1):
        if i == 0 or i == 1:
            fac_list.append(i)
        else:
            fac_list.append(fac_list[i - 1] * i)

    print(fac_list)
    return fac_list[n]

print(factorial(5))