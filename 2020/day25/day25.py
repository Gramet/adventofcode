with open("input", "r") as f:
    lines = f.readlines()

card_key = int(lines[0])
door_key = int(lines[1])


def find_loopsize(key, init=7):
    val = 1
    i = 0
    while val != key:
        val *= init
        val = val % 20201227
        i += 1
    return i


card_loop = find_loopsize(card_key, 7)

val = 1
for i in range(card_loop):
    val *= door_key
    val = val % 20201227

print(val)
