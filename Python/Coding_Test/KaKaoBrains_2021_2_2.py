import json
import requests

def getTopRatedFoodOutlets(city):
    # Write your code here
    url = 'https://jsonmock.hackerrank.com/api/food_outlets?'
    req = requests.get(url + 'city=' + city)
    j = req.json()
    rating = list()

    for i in range(j['total_pages']):
        req = requests.get(url + 'city=' + city + '&page=' + str(i))
        j = req.json()
        rating.extend(j['data'])

    print(rating)
    rating_rank = list()

    for i in range(len(rating)):
        tmp_dict = rating[i]['user_rating']
        tmp_rating = float(tmp_dict['average_rating'])
        rating_rank.append([tmp_rating, [rating[i]['name'], rating[i]['id']]])

    rating_rank.sort(key=lambda x:x[0])
    print(rating_rank)

    cnt = 0  # 0 < rank <= 5
    answer = list()
    tmp_max = rating_rank[-1][0]
    tmp_lst = list()
    for i in range(1, len(rating_rank) + 1):
        if tmp_max == rating_rank[-i][0]:  # if two ratings is equal, check API input order
            tmp_lst.append([rating_rank[-i][1][1], rating_rank[-i][1][0]])

        else:
            tmp_lst.sort(key=lambda x: x[0])

            for k in range(len(tmp_lst)):
                answer.append(tmp_lst[k][1])
                cnt += 1
                if cnt >= 5:
                    break

            if cnt >= 5:
                break

            tmp_lst = [(rating_rank[-i][1][1], rating_rank[-i][1][0])]
            tmp_max = rating_rank[-i][0]

    return answer


if __name__ == '__main__':
    print(getTopRatedFoodOutlets('Denver'))