from pathlib import Path

import numpy as np


def is_in_range(val, ranges):
    return ranges[0][0] <= val <= ranges[0][1] or ranges[1][0] <= val <= ranges[1][1]


class Solution:
    def __init__(self):
        with open(Path(__file__).parent / "input", "r") as f:
            self.input = f.readlines()

        self.rules = {}
        for i, line in enumerate(self.input):
            if line == "\n":
                break
            name, rest = line.strip().split(":")
            range1, range2 = rest.split(" or ")
            min1, max1 = range1.split("-")
            min2, max2 = range2.split("-")
            self.rules[name] = [[int(min1), int(max1)], [int(min2), int(max2)]]

        self.mytick = [int(x) for x in self.input[i + 2].strip().split(",")]
        self.start_ticks = i + 5

    def solve_part_1(self):
        invalid_vals = []
        self.valid_ticks = []
        for line in self.input[self.start_ticks :]:
            is_valid_tick = True
            vals = [int(x) for x in line.strip().split(",")]
            for val in vals:
                is_valid = False
                for ranges in self.rules.values():
                    if is_in_range(val, ranges):
                        is_valid = True
                if not is_valid:
                    invalid_vals.append(val)
                    is_valid_tick = False
            if is_valid_tick:
                self.valid_ticks.append(vals)
        answer = sum(invalid_vals)
        print(answer)
        return answer

    def solve_part_2(self):
        valid_ticks = np.array(self.valid_ticks)
        field_pos = {}
        for field, ranges in self.rules.items():
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

        answer = 1
        for k, v in field_pos.items():
            if k.startswith("departure"):
                answer *= self.mytick[v[0]]
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
