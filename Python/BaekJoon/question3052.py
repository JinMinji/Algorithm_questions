#나머지, 브론즈2
import sys


if __name__ == "__main__":
    remains = list()
    for i in range(10):
        a = int(sys.stdin.readline())
        a %= 42
        remains.append(a)

    remains = set(remains)

    print(len(remains))