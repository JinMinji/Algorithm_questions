def solution(n, k, cmd):
    data = ['O'] * n
    changed_data = [i for i in range(n)]
    cur_cursor = k
    C_log = list()  # 'Z'를 통한 삭제(C) 복구를 위해 로그를 담아줄 list

    for command in cmd:
        if command[0] == 'U':
            cur_cursor -= int(command[2])
            if cur_cursor < 0:
                cur_cursor = 0

        if command[0] == 'D':
            cur_cursor += int(command[2])
            if cur_cursor >= len(changed_data):
                cur_cursor = len(changed_data)-1

        if command[0] == 'C':
            data[changed_data[cur_cursor]] = 'X'
            C_log.append(changed_data[cur_cursor])
            if cur_cursor == len(changed_data)-1:
                cur_cursor -= 1
            else:
                cur_cursor += 1

        if command[0] == 'Z':
            if len(C_log) > 0:
                rollback_index = C_log.pop()
                data[rollback_index] = 'O'
                if rollback_index > changed_data[-1]:
                    changed_data.append(rollback_index)
                else:
                    for i in range(0, len(changed_data)-1):
                        if rollback_index < changed_data[i]:
                            changed_data.insert(i,rollback_index)

                if changed_data[cur_cursor] > rollback_index:
                    cur_cursor += 1



    answer = ''.join(data)

    return answer

if __name__ == "__main__":
    n = 8
    k = 2
    cmd = ["D 2","C","U 3","C","D 4","C","U 2","Z","Z","U 1","C"]
    print(solution(n, k, cmd))