def get_contained(bag_str, rules):

    list_contain = set([])
    for bag in rules:
        if bag_str in rules[bag]:
            list_contain.add(bag)
    if list_contain == set([]):
        return list_contain
    else:
        for cnt in list_contain:
            list_contain = list_contain | get_contained(cnt, rules)

    return list_contain


def get_content(bag_str, rules):

    content = 0
    if bag_str not in rules:
        return content
    else:
        for k, v in rules[bag_str].items():
            content += v + v * get_content(k, rules)
        return content


rules = {}
with open("input", "r") as f:
    lines = f.readlines()

for line in lines:
    if "no other bags" in line:
        continue
    line = line.replace("bags", "bag")
    line = line.strip(".\n")
    bag = line.split(" contain")[0]
    content = line.split(" contain")[1]
    contents = content.split(",")
    bag_ct = {}
    for c in contents:
        num = int(c.split(" ")[1])
        c_type = " ".join(c.split(" ")[2:])
        bag_ct[c_type] = num
    rules[bag] = bag_ct

can_contain_shiny_gold = get_contained("shiny gold bag", rules)
print(f"{len(can_contain_shiny_gold)} can contain  shiny gold bag")
print(f"{get_content('shiny gold bag', rules)} are contained in a shiny gold bag")
