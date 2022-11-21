with open("input", "r") as f:
    lines = f.readlines()

p1 = []
p2 = []

second = False
for line in lines[1:]:
    if line == "\n" or line.startswith("Player"):
        second = True
        continue

    if second:
        p2.append(int(line))
    else:
        p1.append(int(line))

while len(p1) > 0 and len(p2) > 0:
    c1 = p1.pop(0)
    c2 = p2.pop(0)

    if c1 > c2:
        p1.append(c1)
        p1.append(c2)
    else:
        p2.append(c2)
        p2.append(c1)

s = 0
if p1:
    for i, c in enumerate(p1[::-1]):
        s += (i + 1) * c
else:
    for i, c in enumerate(p2[::-1]):
        s += (i + 1) * c
print(f"Part 1 : {s}")

p1 = []
p2 = []

second = False
for line in lines[1:]:
    if line == "\n" or line.startswith("Player"):
        second = True
        continue

    if second:
        p2.append(int(line))
    else:
        p1.append(int(line))


def recursive_combat(p1, p2):
    played_games = set()

    while len(p1) > 0 and len(p2) > 0:

        if hash((tuple(p1), tuple(p2))) in played_games:
            print("Game already played")
            print(played_games)
            return p1, []

        played_games.add(hash((tuple(p1), tuple(p2))))
        c1 = p1.pop(0)
        c2 = p2.pop(0)

        if c1 <= len(p1) and c2 <= len(p2):
            print(f"P1: {c1}, P2: {c2}, recursing with {p1[:c1]}, {p2[:c2]}")
            tmp1, tmp2 = recursive_combat(p1[:c1], p2[:c2])
            if tmp1:
                p1.append(c1)
                p1.append(c2)
            else:
                p2.append(c2)
                p2.append(c1)
        else:
            print(f"Playing: {c1} vs {c2}")
            print(p1, p2)
            if c1 > c2:
                p1.append(c1)
                p1.append(c2)
            else:
                p2.append(c2)
                p2.append(c1)
            print(f"{p1}, {p2}")

    return p1, p2


p1, p2 = recursive_combat(p1, p2)

print(p1, p2)
s = 0
if p1:
    for i, c in enumerate(p1[::-1]):
        s += (i + 1) * c
else:
    for i, c in enumerate(p2[::-1]):
        s += (i + 1) * c
print(f"Part 2 : {s}")
