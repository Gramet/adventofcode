from functools import cache
from pathlib import Path

from aoc_utils import *

INPUT_FILE = Path(__file__).parent / "input"


def num_arrangements(line) -> int:
    springs, arrangement = line.strip("\n").split()
    arrangement = tuple(map(int, arrangement.split(",")))
    return compute_num_arrangements(springs, arrangement)


@cache
def compute_num_arrangements(springs, spring_nums) -> int:
    springs = springs.lstrip(".")  # get rid of leading "."

    if len(springs) == 0:
        return int(len(spring_nums) == 0)  # Ok if empty string but no more springs

    if len(spring_nums) == 0:
        return int(
            "#" not in springs
        )  # Ok if no more spring to search and no spring in string

    if springs[0] == "?":  # replace "?" with both possible values
        return compute_num_arrangements(
            "#" + springs[1:], spring_nums
        ) + compute_num_arrangements("." + springs[1:], spring_nums)

    # Only # leads left
    if len(springs) < sum(spring_nums) or "." in springs[: spring_nums[0]]:
        return 0  # Not enough space to fit springs
    if len(springs) == spring_nums[0]:
        return int(len(spring_nums) == 1)  # last springs fits perfectly
    if springs[spring_nums[0]] == "#":
        return 0  # Must be "." or "?"

    return compute_num_arrangements(springs[spring_nums[0] + 1 :], spring_nums[1:])


class Solution:
    def __init__(self):
        self.input = read_input(INPUT_FILE)

    def solve_part_1(self):
        answer = 0
        for line in self.input:
            num = num_arrangements(line)
            answer += num
        print(answer)
        return answer

    def solve_part_2(self):
        answer = 0
        for line in self.input:
            springs, arrangement = line.strip("\n").split()
            springs = "?".join([springs] * 5)
            arrangement = ",".join([arrangement] * 5)
            line = springs + " " + arrangement
            num = num_arrangements(line)
            answer += num
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
