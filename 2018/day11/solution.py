from pathlib import Path

from aoc_utils import *
from functools import cache
from tqdm import tqdm

INPUT_FILE = Path(__file__).parent / "input"


class Solution:
    def __init__(self):
        self.input = read_input(INPUT_FILE)
        self.grid_num = int(self.input[0])
        self.grid_power = [
            [self.compute_power(x, y) for x in range(1, 301)] for y in range(1, 301)
        ]
        print(len(self.grid_power), len(self.grid_power[0]))

    @cache
    def compute_power(self, x, y):
        power = (((x + 10) * y + self.grid_num) * (x + 10) // 100) % 10 - 5
        return power

    @cache
    def compute_power_square(self, x, y, size):
        if size == 1:
            return self.grid_power[y - 1][x - 1]
        else:
            # print(x, y, size)

            return (
                self.compute_power_square(x, y, size - 1)
                + sum(
                    self.grid_power[y + size - 2][x_ - 1] for x_ in range(x, x + size)
                )
                + sum(
                    self.grid_power[y_ - 1][x + size - 2] for y_ in range(y, y + size)
                )
                - self.grid_power[y + size - 2][x + size - 2]
            )

    def solve_part_1(self):
        cur_max = 0
        for x in range(1, 299):
            for y in range(1, 299):
                if (power := self.compute_power_square(x, y, 3)) > cur_max:
                    cur_best = (x, y)
                    cur_max = power
                    print(power, cur_best)

        answer = f"{cur_best[0]},{cur_best[1]}"
        print(answer)
        return answer

    def solve_part_2(self):
        cur_max = 0
        for size in tqdm(range(1, 300)):
            for x in range(1, 301 - size):
                for y in range(1, 301 - size):
                    if (power := self.compute_power_square(x, y, size)) > cur_max:
                        cur_best = (x, y, size)
                        cur_max = power
                        print(power, cur_best)

        answer = f"{cur_best[0]},{cur_best[1]},{cur_best[2]}"
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
