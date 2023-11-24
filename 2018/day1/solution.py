import itertools
from pathlib import Path

from aoc_utils import *

INPUT_FILE = Path(__file__).parent / "input"


class Solution:
    def __init__(self):
        self.input = read_ints(INPUT_FILE)

    def solve_part_1(self):
        answer = sum(self.input)
        print(answer)
        return answer

    def solve_part_2(self):
        seen = set([0])
        answer = 0
        for next_val in itertools.cycle(self.input):
            answer += next_val
            if answer in seen:
                break
            seen.add(answer)

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
