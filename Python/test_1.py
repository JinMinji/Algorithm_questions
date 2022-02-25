import copy

stack_1 = list()
stack_2 = list()


def make_queue(type, val):
    if type == 'push':
        stack_1.append(val)

    if type == 'pop':
        # tmp_stack = copy.deepcopy(stack_1)
        for i in range(len(stack_1)):
            stack_2.append(stack_1.pop())

        return stack_2.pop()

    return


if __name__ == '__main__':
    make_queue('push', 1)
    make_queue('push', 2)
    make_queue('push', 3)

    print(make_queue('pop', ''))

    print(make_queue('pop', ''))





