p = 53
q = 97
message = "!L0VEH@RRYP0TTER"
e = 65537

n = p * q
encrypted_values = []
for i in message:
    c = ((ord(i) + 1000) ** e) % n
    c = ((c + 1000) ** e) % n
    c = ((c + 1000) ** e) % n
    encrypted_values.append(c)

print(encrypted_values)
