# 피보나치 수 3, 골드 2
# 피사노 주기
# 피보나치 수를 K로 나눈 나머지는 항상 주기를 가진다.
# 주기가 P면 N번째 피보나치수를 M으로 나눈 나머지는 N%P번째 피보나치수를 M으로 나눈 나머지와 같다.
# M = 10**k일 때, k > 2라면 주기 P는 항상 15*(10**k-1)이다.

if __name__ == '__main__':
    n = int(input())
    fibo = [0, 1]

    p = 1000000//10*15

    for i in range(2, p):
        fibo.append((fibo[i-1]+fibo[i-2]) % 1000000)

    print(fibo[n%p])