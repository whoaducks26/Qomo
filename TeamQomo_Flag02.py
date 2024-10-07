seats = eval(input("Input seats: "))
enchanted_rows = eval(input("Input enchanted rows: "))

def can_see_stage(seats, enchanted_rows):
    for i in enchanted_rows:
        for j in range(len(seats[i])):
            if seats[i][j] - seats[i-1][j] < 2:
                return False
            else:
                continue
    return True

can_see_stage(seats,enchanted_rows)
