# Plase note that external libraries, such as NumPy or Pandas
# are NOT available for this task

# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")


def solution(S):
    # write your code in Python 3.6
    cities = dict()
    S = S.replace(",", "")
    S_list = S.split("\n")
    # print(S_list)

    for i in range(len(S_list)):
        s = S_list[i]
        # 각 정보 분리
        tmp_info = s.split(' ')
        # 확장자
        extension = tmp_info[0].split('.')[1]
        # 도시
        city = tmp_info[1]
        # 시간
        time = tmp_info[2].split("-") + tmp_info[3].split(":")
        time = int("".join(time))

        # print(time)

        if city in cities.keys():
            cities[city].append([time, extension, i])
        else:
            cities[city] = [[time, extension, i]]

    answer = ["" for i in range(len(S_list))]

    for key, value in cities.items():
        max_len = len(str(len(value)))
        value.sort()  # 시간 순으로 sort, 빠른게 먼저!
        for i in range(len(value)):
            v = value[i]
            answer[v[2]] = key + str((i + 1)).zfill(max_len) + "." + v[1]

    result = ""
    for i in range(len(answer) - 1):
        result += answer[i] + "\n"

    result += answer[-1]

    return result


if __name__ == "__main__":
    print(solution('photo.jpg, Warsaw, 2013-09-05 14:08:15\njohn.png, London, 2015-06-20 15:13:22\nmyFriends.png, Warsaw, 2013-09-05 14:07:13\nEiffel.jpg, Paris, 2015-07-23 08:03:02\npisatower.jpg, Paris, 2015-07-22 23:59:59\nBOB.jpg, London, 2015-08-05 00:02:03\nnotredame.png, Paris, 2015-09-01 12:00:00\nme.jpg, Warsaw, 2013-09-06 15:40:22\na.png, Warsaw, 2016-02-13 13:33:50\nb.jpg, Warsaw, 2016-01-02 15:12:22\nc.jpg, Warsaw, 2016-01-02 14:34:30\nd.jpg, Warsaw, 2016-01-02 15:15:01\ne.png, Warsaw, 2016-01-02 09:49:09\nf.png, Warsaw, 2016-01-02 10:55:32\ng.jpg, Warsaw, 2016-02-29 22:13:11'))