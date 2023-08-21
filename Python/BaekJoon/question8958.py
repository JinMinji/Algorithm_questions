#OX퀴즈, 브론즈 2
import sys


if __name__ == "__main__":
    N = int(input())

    for i in range(N):
        result = sys.stdin.readline()
        score = 0
        con_o = 0
        for r in result:
            if r == "O":
                con_o += 1
                score += con_o
            else:
                con_o = 0

        print(score)