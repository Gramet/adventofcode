import numpy as np

with open("input", "r") as f:
    lines = f.readlines()


rules = {}
for i, line in enumerate(lines):
    if line == "\n":
        break
    name, rest = line.strip().split(":")
    range1, range2 = rest.split(" or ")
    min1, max1 = range1.split("-")
    min2, max2 = range2.split("-")
    rules[name] = [[int(min1), int(max1)], [int(min2), int(max2)]]

mytick = [int(x) for x in lines[i + 2].strip().split(",")]


def is_in_range(val, ranges):
    return ranges[0][0] <= val <= ranges[0][1] or ranges[1][0] <= val <= ranges[1][1]


invalid_vals = []
valid_ticks = []
for i2, line in enumerate(lines[i + 5 :]):
    is_valid_tick = True
    vals = [int(x) for x in line.strip().split(",")]
    for val in vals:
        is_valid = False
        for name, ranges in rules.items():
            if is_in_range(val, ranges):
                is_valid = True
        if not is_valid:
            invalid_vals.append(val)
            is_valid_tick = False
    if is_valid_tick:
        valid_ticks.append(vals)

print(sum(invalid_vals))


valid_ticks = np.array(valid_ticks)
field_pos = {}
for field, ranges in rules.items():
    for pos in range(len(valid_ticks[0])):
        if all(is_in_range(x, ranges) for x in valid_ticks[:, pos]):
            field_pos[field] = field_pos.get(field, []) + [pos]

while not all(len(x) == 1 for x in field_pos.values()):
    for k, v in field_pos.items():
        if len(v) == 1:
            for k2, v2 in field_pos.items():
                if k == k2:
                    continue
                try:
                    v2.remove(v[0])
                except ValueError:
                    pass


p = 1
for k, v in field_pos.items():
    if k.startswith("departure"):
        p *= mytick[v[0]]

print(p)
