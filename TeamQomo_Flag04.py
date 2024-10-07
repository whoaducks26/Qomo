# Flag 4

riddle_num = 10

alpha = "a b c d e f g h i j k l m n o p q r s t u v w x y z"
arr = alpha.split(" ")
# print(arr)
message = "S vyfo Robwsyxo Qbkxqob!"
new_message = ""

for char in message:
    if char.isalpha():
        if char.islower():
            temp_num = arr.index(char)
            ori_num = temp_num-10
            new_message += arr[ori_num]
        else:
            temp_num = ord(char)
            ori_num = temp_num-10
            new_message += chr(ori_num)
    else:
        new_message += char

print(new_message)
