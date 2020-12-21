with open("input", "r") as f:
    lines = f.readlines()


allergens = {}
all_ingrs = set()
all_compos = []
for line in lines:
    compo, rest = line.split(" (contains ")
    allergs = rest.strip().strip(")").split(", ")
    ingrs = set(compo.split())
    all_compos.append(ingrs)
    all_ingrs = all_ingrs | ingrs
    for a in allergs:
        if a in allergens:
            allergens[a] = allergens[a] & ingrs
        else:
            allergens[a] = ingrs

found = {}
while len(found) < len(allergens):
    for a, ingrs in allergens.items():
        if len(ingrs) == 1:
            found[a] = ingrs
            for b, ingrs_b in allergens.items():
                if b == a:
                    continue
                allergens[b] = ingrs_b - ingrs


safe_ingrs = all_ingrs.difference(list(x)[0] for x in found.values())

count_safe = 0
for compo in all_compos:
    for ingr in safe_ingrs:
        if ingr in compo:
            count_safe += 1

print(count_safe)

s = ""
for k, v in sorted(found.items()):
    print(k, v)
    s += list(v)[0] + ","

s = s[:-1]
print(s)
