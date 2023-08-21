# Σ, 골드4
# 먼소리야;;
import sys
from math import gcd


def power(n, e):
    if e == 0:
        return 1
    elif e == 1:
        return n
    elif e % 2:
        return n * power(n, e - 1) % mod
    else:
        t = power(n, e // 2)
        return t * t % mod


def modular_inverse(a):
    global mod

    for i in range(mod):
        if (a*i) % mod == 1:
            return a * i % mod


if __name__ == "__main__":
    M = int(input())
    mod = 1_000_000_007

    ans = 0
    for i in range(M):
        n, s = map(int, sys.stdin.readline().split())

        tmp = gcd(n, s) #기약분수 만들기. 최대 공약수로 나눠 준다.
        n //= tmp
        s //= tmp

        ans += s*power(n, mod-2) % mod
        ans %= mod

    print(ans)
