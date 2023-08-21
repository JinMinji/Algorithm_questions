#트리의 순회, 골드 2
import sys


def make_pre_order(in_o, post_o):
    result = list()

    return result


if __name__ == "__main__":
    n = int(input())

    in_order = list(map(int, sys.stdin.readline().split()))
    post_order = list(map(int, sys.stdin.readline().split()))

    print(*make_pre_order(in_order, post_order))