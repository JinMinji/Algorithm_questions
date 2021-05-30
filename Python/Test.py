import itertools

index_map = [[0,0],[0,1],[0,2]
    ,[1,0],[1,1],[1,2]
    ,[2,0],[2,1],[2,2]
             ]

all_com = list(itertools.combinations(index_map, 5))
print(all_com)

