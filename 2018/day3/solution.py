from collections import defaultdict
from pathlib import Path

from aoc_utils import *

INPUT_FILE = Path(__file__).parent / "input"


class Solution:
    def __init__(self):
        self.input = read_input(INPUT_FILE)

    def solve_part_1(self):
        self.map = defaultdict(int)
        for order in self.input:
            _, w_start, h_start, width, height = parse_ints(order)
            for w in range(width):
                for h in range(height):
                    self.map[(w_start + w, h_start + h)] += 1

        answer = sum([x > 1 for x in self.map.values()])
        print(answer)
        return answer

    def solve_part_2(self):
        for order in self.input:
            id, w_start, h_start, width, height = parse_ints(order)
            if any(
                self.map[(w_start + w, h_start + h)] != 1
                for w in range(width)
                for h in range(height)
            ):
                continue
            else:
                answer = id
                break

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
