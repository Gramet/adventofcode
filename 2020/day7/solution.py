from pathlib import Path


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


def build_rules(lines):
    rules = {}
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
    return rules


class Solution:
    def __init__(self):
        with open(Path(__file__).parent / "input", "r") as f:
            self.input = f.readlines()

        self.rules = build_rules(self.input)

    def solve_part_1(self):
        answer = len(get_contained("shiny gold bag", self.rules))
        print(answer)
        return answer

    def solve_part_2(self):
        answer = get_content("shiny gold bag", self.rules)
        print(answer)
        return answer

    def save_results(self):
        with open(Path(__file__).parent / "part1", "w") as opened_file:
            opened_file.write(str(self.solve_part_1()))

        with open(Path(__file__).parent / "part2", "w") as opened_file:
            opened_file.write(str(self.solve_part_2()))


if __name__ == "__main__":
    solution = Solution()
    solution.save_results()
