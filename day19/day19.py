import itertools

with open("input", "r") as f:
    lines = [l.strip() for l in f.readlines()]

rules = {}

for i, line in enumerate(lines):
    if line == "":
        break
    num, rule = line.split(": ")
    rules[num] = [seq.split(" ") for seq in rule.split(" | ")]


def check(rules, id, string, start):
    rule_to_check = rules[id]
    if rule_to_check[0][0][0] == '"':
        return (
            {start + 1}
            if start < len(string) and rule_to_check[0][0][1] == string[start]
            else set([])
        )
    else:
        ends = []
        for subrule in rule_to_check:
            buffer = {start}
            for part in subrule:
                temp = set([])
                for idx in buffer:
                    temp = temp | check(rules, part, string, idx)
                buffer = temp
            ends.append(buffer)
        ends = set(itertools.chain(*ends))
        return ends


res = sum([len(string) in check(rules, "0", string, 0) for string in lines[i + 1 :]])
print(res)

rules["8"] = [["42"], ["42", "8"]]
rules["11"] = [["42", "31"], ["42", "11", "31"]]
res = sum([len(string) in check(rules, "0", string, 0) for string in lines[i + 1 :]])
print(res)
