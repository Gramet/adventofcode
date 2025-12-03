from pathlib import Path

from aoc_utils import *

INPUT_FILE = Path(__file__).parent / "input"


def max_joltage(batteries, num_to_turn_on):
    if num_to_turn_on == 1:
        return max(batteries)
    for val in sorted(set(batteries), reverse=True):
        val_idx = batteries.index(val)
        if val_idx < len(batteries) - (num_to_turn_on - 1):
            return 10 ** (num_to_turn_on - 1) * val + max_joltage(
                batteries[val_idx + 1 :], num_to_turn_on - 1
            )


class Solution:
    def __init__(self):
        self.input = read_input(INPUT_FILE)

    def solve_part_1(self):
        answer = 0
        for bank in self.input:
            batteries = [int(x) for x in bank[:-1]]
            joltage = max_joltage(batteries, 2)
            answer += joltage
        print(answer)
        return answer

    def solve_part_2(self):
        answer = 0
        for bank in self.input:
            batteries = [int(x) for x in bank[:-1]]
            joltage = max_joltage(batteries, 12)
            answer += joltage
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
