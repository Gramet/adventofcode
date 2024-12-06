from pathlib import Path

from aoc_utils import *

INPUT_FILE = Path(__file__).parent / "input"

XMAS = "XMAS"


class Solution:
    def __init__(self):
        self.input = read_input(INPUT_FILE)

    def solve_part_1(self):
        answer = 0
        for dir in deltas8_2d:
            for x, line in enumerate(self.input):
                for y, chr in enumerate(line.strip("\n")):
                    if (
                        chr == "X"
                        and 0 <= x + 3 * dir[0] <= len(self.input) - 1
                        and 0 <= y + 3 * dir[1] <= len(line) - 1
                        and self.input[x + dir[0]][y + dir[1]] == "M"
                        and self.input[x + 2 * dir[0]][y + 2 * dir[1]] == "A"
                        and self.input[x + 3 * dir[0]][y + 3 * dir[1]] == "S"
                    ):
                        answer += 1
        print(answer)
        return answer

    def solve_part_2(self):
        answer = 0
        for x, line in enumerate(self.input):
            for y, chr in enumerate(line.strip("\n")):
                if (
                    0 < x < len(self.input) - 1
                    and 0 < y < len(line) - 2
                    and chr == "A"
                    and (
                        (
                            self.input[x - 1][y - 1] == "M"
                            and self.input[x - 1][y + 1] == "M"
                            and self.input[x + 1][y + 1] == "S"
                            and self.input[x + 1][y - 1] == "S"
                        )
                        or (
                            self.input[x - 1][y - 1] == "S"
                            and self.input[x - 1][y + 1] == "S"
                            and self.input[x + 1][y + 1] == "M"
                            and self.input[x + 1][y - 1] == "M"
                        )
                        or (
                            self.input[x - 1][y - 1] == "M"
                            and self.input[x - 1][y + 1] == "S"
                            and self.input[x + 1][y + 1] == "S"
                            and self.input[x + 1][y - 1] == "M"
                        )
                        or (
                            self.input[x - 1][y - 1] == "S"
                            and self.input[x - 1][y + 1] == "M"
                            and self.input[x + 1][y + 1] == "M"
                            and self.input[x + 1][y - 1] == "S"
                        )
                    )
                ):
                    answer += 1
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
