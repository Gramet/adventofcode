import math
import re
from pathlib import Path

from aoc_utils import *

INPUT_FILE = Path(__file__).parent / "input"


class Solution:
    def __init__(self):
        self.input = read_input(INPUT_FILE)

    def solve_part_1(self):
        numbers1 = parse_ints(self.input[0])
        numbers2 = parse_ints(self.input[1])
        numbers3 = parse_ints(self.input[2])
        numbers4 = parse_ints(self.input[3])
        ops = re.findall(r"[\*\+]", self.input[4])
        answer = 0
        for num1, num2, num3, num4, op in zip(
            numbers1, numbers2, numbers3, numbers4, ops
        ):
            if op == "+":
                answer += num1 + num2 + num3 + num4
            else:
                answer += num1 * num2 * num3 * num4
        print(answer)
        return answer

    def solve_part_2(self):
        nums = []
        answer = 0
        op = None
        for col in range(len(self.input[0])):
            if self.input[4][col] in "+*":
                op = self.input[4][col]
            if all(self.input[row][col] == " " for row in range(4)):
                if op == "+":
                    answer += sum(nums)
                else:
                    answer += math.prod(nums)
                nums = []

            num = (
                int(self.input[0][col] if self.input[0][col].isdigit() else "0") * 1000
                + int(self.input[1][col] if self.input[1][col].isdigit() else "0") * 100
                + int(self.input[2][col] if self.input[2][col].isdigit() else "0") * 10
                + int(self.input[3][col] if self.input[3][col].isdigit() else "0")
            )
            if self.input[3][col] == " ":
                num /= 10
                if self.input[2][col] == " ":
                    num /= 10
                    if self.input[1][col] == " ":
                        num /= 10
            if num != 0:
                nums.append(num)
        if op == "+":
            answer += sum(nums)
        else:
            answer += math.prod(nums)
        nums = []

        print(int(answer))
        return int(answer)

    def save_results(self):
        with open(Path(__file__).parent / "part1", "w") as opened_file:
            opened_file.write(str(self.solve_part_1()))

        with open(Path(__file__).parent / "part2", "w") as opened_file:
            opened_file.write(str(self.solve_part_2()))


if __name__ == "__main__":
    solution = Solution()
    solution.save_results()
