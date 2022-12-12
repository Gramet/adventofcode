import itertools
from pathlib import Path


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


class Solution:
    def __init__(self):
        with open(Path(__file__).parent / "input", "r") as f:
            self.input = [l.strip() for l in f.readlines()]

        self.rules = {}

        for i, line in enumerate(self.input):
            if line == "":
                break
            num, rule = line.split(": ")
            self.rules[num] = [seq.split(" ") for seq in rule.split(" | ")]

        self.idx_start = i

    def solve_part_1(self):
        answer = sum(
            [
                len(string) in check(self.rules, "0", string, 0)
                for string in self.input[self.idx_start + 1 :]
            ]
        )
        print(answer)
        return answer

    def solve_part_2(self):
        self.rules["8"] = [["42"], ["42", "8"]]
        self.rules["11"] = [["42", "31"], ["42", "11", "31"]]
        answer = sum(
            [
                len(string) in check(self.rules, "0", string, 0)
                for string in self.input[self.idx_start + 1 :]
            ]
        )
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
