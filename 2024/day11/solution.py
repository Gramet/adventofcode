from functools import cache
from pathlib import Path

from aoc_utils import *

INPUT_FILE = Path(__file__).parent / "input"


@cache
def compute_stone(stone, blink, max_blink):
    if blink == max_blink:
        return 1

    if stone == 0:
        return compute_stone(1, blink + 1, max_blink)
    elif len(str(stone)) % 2 == 0:
        return compute_stone(
            int(str(stone)[: len(str(stone)) // 2]), blink + 1, max_blink
        ) + compute_stone(int(str(stone)[len(str(stone)) // 2 :]), blink + 1, max_blink)
    else:
        return compute_stone(stone * 2024, blink + 1, max_blink)


class Solution:
    def __init__(self):
        self.input = read_input(INPUT_FILE)
        self.stones = parse_ints(self.input[0])

    def solve_part_1(self):
        answer = 0
        for stone in self.stones:
            answer += compute_stone(stone, 0, 25)
        print(answer)
        return answer

    def solve_part_2(self):
        answer = 0
        for stone in self.stones:
            answer += compute_stone(stone, 0, 75)
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
