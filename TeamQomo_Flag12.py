rune_list = [
    10, 'cursed', 40, 'broken', 20, 'none', 30, ['trick', 20, 30]
    ]

target_value = 0

for i in range(len(rune_list)):
    try:
        if type(rune_list[i]) == list:
            for j in range(len(rune_list[i])):
                try:
                    target_value += rune_list[i][j]
                except TypeError:
                    continue

        target_value += rune_list[i]

    except TypeError:
        continue
    

print(target_value)
#GIT{Failed to decode the rune because the target is now CURRENT_TOTAL}
