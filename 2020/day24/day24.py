from copy import deepcopy

with open("input", "r") as f:
    lines = [line.strip() for line in f.readlines()]

coos = []
for line_num, line in enumerate(lines):
    coos.append({"e": 0, "se": 0, "ne": 0})
    i = 0
    while i < len(line):
        if line[i] == "e":
            coos[line_num]["e"] += 1
            i += 1
        elif line[i] == "w":
            coos[line_num]["e"] -= 1
            i += 1
        elif line[i : i + 2] == "se":
            coos[line_num]["se"] += 1
            i += 2
        elif line[i : i + 2] == "nw":
            coos[line_num]["se"] -= 1
            i += 2
        elif line[i : i + 2] == "ne":
            coos[line_num]["ne"] += 1
            i += 2
        elif line[i : i + 2] == "sw":
            coos[line_num]["ne"] -= 1
            i += 2


def reduce(coos):
    for coo in coos:
        if coo["se"] > 0:
            while coo["se"] != 0:
                coo["ne"] -= 1
                coo["e"] += 1
                coo["se"] -= 1
        elif coo["se"] < 0:
            while coo["se"] != 0:
                coo["ne"] += 1
                coo["e"] -= 1
                coo["se"] += 1
    return coos


coos = reduce(coos)
print(coos)
black = []
for tile in coos:
    if tile not in black:
        black.append(tile)
    else:
        black.remove(tile)

print(len(black))


def get_neighbours(tiles):
    neighs = []
    for tile in tiles:
        neigh_e = deepcopy(tile)
        neigh_w = deepcopy(tile)
        neigh_se = deepcopy(tile)
        neigh_ne = deepcopy(tile)
        neigh_nw = deepcopy(tile)
        neigh_sw = deepcopy(tile)

        neigh_e["e"] += 1
        neigh_w["e"] -= 1
        neigh_se["e"] += 1
        neigh_se["ne"] -= 1
        neigh_ne["ne"] += 1
        neigh_nw["ne"] += 1
        neigh_nw["e"] -= 1
        neigh_sw["ne"] -= 1
        neighs += [neigh_e, neigh_se, neigh_w, neigh_ne, neigh_nw, neigh_sw]

    return neighs


for day in range(100):
    neighbours = get_neighbours(black)
    new_black = []
    for black_tile in black:
        if 0 < neighbours.count(black_tile) <= 2:
            new_black.append(black_tile)

    for neigh in neighbours:
        if (
            neighbours.count(neigh) == 2
            and (neigh not in black)
            and (neigh not in new_black)
        ):
            new_black.append(neigh)

    black = new_black
    print(f"Day {day}: {len(black)} black tiles")
