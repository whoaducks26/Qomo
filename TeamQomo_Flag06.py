# Flag 6

# fixed code
def sort_crystals_by_power(crystal_powers):
    positive_powers = [p for p in crystal_powers if int(p) >= 0]
    # print(positive_powers)
    negative_powers = [p for p in crystal_powers if int(p) < 0]
    # print(negative_powers)
    # sorted_powers = positive_powers.sort()
    positive_powers.sort(reverse=True)
    # print(positive_powers)
    final_powers = positive_powers + negative_powers
    print(final_powers)
    return "GIT{"+f"{final_powers[0]}_{final_powers[-1]}"+"}"

crystal_powers = ["15", "42", "-9", "33", "57", "-23"]
sorted_crystals = sort_crystals_by_power(crystal_powers)
print(sorted_crystals)
