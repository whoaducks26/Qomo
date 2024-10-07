# flag 10

artifacts = [(1, 10, 2),
             (2, 20, 3),
             (3, 15, 1),
             (4, 30, 4),
             (5, 25, 2)]

max_weight = 6

possible_id_combos = [(1, 2, 3), (2, 3, 5), (1, 4), (4, 5)]

highest = 0
for x in possible_id_combos:
    temp = 0
    for id_num in x:
        points = artifacts[id_num-1][1]
        temp += points
    if temp > highest:
        highest = temp
        ids = x

print(highest)
print(ids)
