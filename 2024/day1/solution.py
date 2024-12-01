from pathlib import Path

from aoc_utils import *

INPUT_FILE = Path(__file__).parent / "input"


class Solution:
    def __init__(self):
        self.input = read_input(INPUT_FILE)

    def solve_part_1(self):
        answer = 0
        self.left_numbers = []
        self.right_numbers = []
        for line in self.input:
            a, b = line.split()
            self.left_numbers.append(int(a))
            self.right_numbers.append(int(b))
        for a, b in zip(sorted(self.left_numbers), sorted(self.right_numbers)):
            answer += abs(int(a) - int(b))
        print(answer)
        return answer

    def solve_part_2(self):
        answer = 0
        for a in self.left_numbers:
            answer += self.right_numbers.count(a) * a
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
