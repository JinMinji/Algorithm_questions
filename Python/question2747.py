input_num = int(input())

fibo = dict()

def fibonacci(num):
    if num in fibo:
        return fibo[num]

    elif num <= 1:
        fibo[num] = num
        return num
    else:
        result = fibonacci(num-1)+fibonacci(num-2)
        fibo[num] = result
        return result

print(fibonacci(input_num))

# 재귀가 아닌 반복문으로 쓰기 -> 시간초과 해결