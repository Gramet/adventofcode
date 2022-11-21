with open("input", "r") as f:
    lines = f.readlines()

timestamp = int(lines[0])

best = timestamp * 2
best_bus = None
for bus in lines[1].strip().split(","):
    if bus == "x":
        continue
    if timestamp % int(bus) == 0:
        print(best, best_bus)
        break
    if int(bus) * (timestamp // int(bus)) + int(bus) < best:
        best = int(bus) * (timestamp // int(bus)) + int(bus)
        best_bus = int(bus)

print(best - timestamp, best_bus, (best - timestamp) * best_bus)

conds = {}
t = 0
prod = 1
for i, bus in enumerate(lines[1].strip().split(",")):
    if bus == "x":
        continue
    conds[i] = int(bus)
    while t % conds[i] != (conds[i] - i) % conds[i]:
        t += prod
    prod *= conds[i]
    print(t, i, conds[i], prod)


print(t)
