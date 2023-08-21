import json
import requests
import heapq


def getTopRatedFoodOutlets(city):
    # Write your code here
    url = 'https://jsonmock.hackerrank.com/api/food_outlets?'
    req = requests.get(url + 'city=' + city)
    j = req.json()
    page_max = j['per_page']
    rating = j['data']

    rating_rank = list()

    for i in range(len(rating)):
        tmp_dict = rating[i]['user_rating']
        tmp_rating = float(tmp_dict['average_rating'])*10
        heapq.heappush(rating_rank, [tmp_rating, [rating[i]['name'], rating[i]['id']]])

    cnt = 0  # 0 < rank <= 5
    answer = list()
    tmp_max = rating_rank[-1][0]
    tmp_lst = list()
    for i in range(1, len(rating_rank) + 1):
        if tmp_max == rating_rank[-i][0]:  # if two ratings is equal, check API input order
            heapq.heappush(tmp_lst, (int(rating_rank[-i][1][1]), rating_rank[-i][1][0]))

        else:
            for k in range(len(tmp_lst)):
                cnt += 1
                answer.append(tmp_lst[k][1])
                if cnt == 5:
                    break

            tmp_lst = [(rating_rank[-i][1][1], rating_rank[-i][1][0])]

    return answer


if __name__ == '__main__':
    print(getTopRatedFoodOutlets('Denver'))