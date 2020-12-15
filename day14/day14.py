with open("input", "r") as f:
    lines = f.readlines()

mem = {}
mask = ""
for line in lines:
    if line.startswith("mask"):
        mask = line.strip().split(" = ")[1]
    elif line.startswith("mem"):
        add = int(line.split("[")[1].split("]")[0])
        val = "{0:b}".format(int(line.strip().split(" = ")[1]))
        val = "0" * (36 - len(val)) + val
        mem[add] = "".join([v if x == "X" else x for x, v in zip(mask, val)])

print(sum(int(v, 2) for v in mem.values()))


def generate_adds(add):
    l = [add]
    while any("X" in a for a in l):
        for a in l:
            if "X" in a:
                l.append(a.replace("X", "0", 1))
                l.append(a.replace("X", "1", 1))
                l.remove(a)

    return l


mem = {}
mask = ""
for line in lines:
    if line.startswith("mask"):
        mask = line.strip().split(" = ")[1]
    elif line.startswith("mem"):
        add = "{0:b}".format(int(line.split("[")[1].split("]")[0]))
        add = "0" * (36 - len(add)) + add
        add = "".join([x if (x == "X" or x == "1") else v for x, v in zip(mask, add)])
        val = "{0:b}".format(int(line.strip().split(" = ")[1]))
        val = "0" * (36 - len(val)) + val
        adds = generate_adds(add)
        for a in adds:
            mem[a] = val


print(sum(int(v, 2) for v in mem.values()))
