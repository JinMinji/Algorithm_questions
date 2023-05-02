# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")
from collections import deque


class Solution(object):
    def __init__(self):
        # write your code in Python 3.6
        self.stack = deque()
        self.transaction = []

    def push(self, value):
        self.stack.append(value)

    def top(self):
        if self.stack:
            return self.stack[-1]
        return 0

    def pop(self):
        if self.stack:
            self.stack.pop()
        return

    def begin(self):
        self.transaction.append(len(self.stack))

    def rollback(self):
        if self.transaction:
            while len(self.stack) != self.transaction[-1]:
                self.stack.pop()
            self.transaction.pop()
            return True
        else:
            return False

    def commit(self):
        if self.transaction:
            self.transaction.pop()
            return True
        else:
            return False


def test():
    # Define your tests here
    sol = Solution()
    sol.push(42)
    assert sol.top() == 42, "top() should be 42"

def example1():
    sol = Solution()
    sol.push(5)
    sol.push(2)                    # stack: [5,2]
    assert sol.top() == 2
    sol.pop()                      # stack: [5]
    assert sol.top() == 5

    sol2 = Solution()
    assert sol2.top() == 0         # top of an empty stack is 0
    sol2.pop()                     # pop should do nothing

def example2():
    sol = Solution()
    sol.push(4)
    sol.begin()                    # start transaction 1
    sol.push(7)                    # stack: [4,7]
    sol.begin()                    # start transaction 2
    sol.push(2)                    # stack: [4,7,2]
    assert sol.rollback() == True  # rollback transaction 2
    assert sol.top() == 7          # stack: [4,7]
    sol.begin()                    # start transaction 3
    sol.push(10)                   # stack: [4,7,10]
    assert sol.commit() == True    # transaction 3 is committed
    assert sol.top() == 10
    assert sol.rollback() == True  # rollback transaction 1
    assert sol.top() == 4          # stack: [4]
    assert sol.commit() == False   # there is no open transaction


if __name__ == "__main__":
    test()
    example1()
    example2()