import re
from pathlib import Path

from aoc_utils import *

INPUT_FILE = Path(__file__).parent / "input"


class Solution:
    def __init__(self):
        self.input = read_input(INPUT_FILE)

    def solve_part_1(self):
        answer = 0
        for line in self.input:
            mul_pattern = r"mul\(\d+,\d+\)"

            for match in re.findall(mul_pattern, line):
                print(match)
                ints = parse_ints(match)
                print(ints)
                answer += ints[0] * ints[1]
        print(answer)
        self.part1 = answer
        return answer

    def solve_part_2(self):
        answer = 0
        full_input = "".join(self.input)
        mul_pattern = r"mul\(\d+,\d+\)|do\(\)|don't\(\)"
        mul_enabled = True
        for match in re.findall(mul_pattern, full_input):
            if match == "don't()":
                mul_enabled = False
            elif match == "do()":
                mul_enabled = True
            elif mul_enabled:
                ints = parse_ints(match)
                print(ints)
                answer += ints[0] * ints[1]
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
