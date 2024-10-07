# flag 11

messed_potion_inventory = {"Polyjuice Potion": "Frost Fern",
                           "Amortentia": "Fire Lily",
                           "Frostbite Elixir": "Phoenix Feather",
                           "Elixir of Life": "Aconite Root",
                           "Firestarter Potion":"Elderflower"}


clean_potion_inventory = {}

for x in messed_potion_inventory:
    first_letter = x[0]
    second_letter = x[1]
    count = 0
    for keys,value in messed_potion_inventory.items():
        if first_letter == value[0]:
            count += 1
        if count == 1:
            clean_potion_inventory[x] = value
        else:
            for keys,value in messed_potion_inventory.items():
                if second_letter == value[1]:
                    clean_potion_inventory[x] = value
        count = 0

print(clean_potion_inventory)
