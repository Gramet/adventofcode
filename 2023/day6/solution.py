from math import ceil, floor, sqrt
from pathlib import Path

from aoc_utils import *

INPUT_FILE = Path(__file__).parent / "input"


class Solution:
    def __init__(self):
        self.input = read_input(INPUT_FILE)

    def solve_part_1(self):
        times = parse_ints(self.input[0])
        distances = parse_ints(self.input[1])
        answer = 1
        for t, d in zip(times, distances):
            h_max = floor(0.5 * (t + sqrt(t**2 - 4 * d)))
            h_min = ceil(0.5 * (t - sqrt(t**2 - 4 * d)))
            answer *= h_max - h_min + 1
        print(answer)
        return answer

    def solve_part_2(self):
        t = parse_ints(self.input[0].replace(" ", ""))[0]
        d = parse_ints(self.input[1].replace(" ", ""))[0]
        print(t, d)
        h_max = floor(0.5 * (t + sqrt(t**2 - 4 * d)))
        h_min = ceil(0.5 * (t - sqrt(t**2 - 4 * d)))
        answer = h_max - h_min + 1
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
