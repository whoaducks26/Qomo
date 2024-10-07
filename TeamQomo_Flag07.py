# Flag 7

dic = {"spells": 
       {"fireball": {"description": "Burns with the fury of a thousand suns","power": "High"},
        "lightning": {"description": "Strikes with the speed of thunder","power": "Medium"},
        "bolt": {"description": "A quick and sharp surge","power": "Low"}},
    "common_spells": 
    {"rays": {"description": "A blazing inferno","power": "High"},
     "explosion": {"description": "A sudden burst","power": "Low"}}}

message = "fireball lightning bolt rays explosion"
msg_arr = message.split(" ")
new = ""

for word in msg_arr:
    if word in dic.get("spells"):
        new += dic.get("spells").get(word)["description"]
    elif word in dic.get("common_spells"):
        new += dic.get("common_spells").get(word)["power"]
    new += " "

new = new.strip(" ")
print("GIT{"+new+"}")
