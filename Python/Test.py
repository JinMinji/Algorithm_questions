from itertools import combinations

temp_list = [i for i in range(1, 21)]

picks = list(combinations(temp_list, 2))
print(len(picks))