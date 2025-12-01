from pathlib import Path

from aoc_utils import *

INPUT_FILE = Path(__file__).parent / "input"


class Solution:
    def __init__(self):
        self.input = read_input(INPUT_FILE)

    def solve_part_1(self):
        val = 50
        answer = 0
        for line in self.input:
            dir = line[0]
            amount = int(line[1:])
            if dir == "R":
                val += amount
                val %= 100
            elif dir == "L":
                val -= amount
                val %= 100
            if val == 0:
                answer += 1
        print(answer)
        return answer

    def solve_part_2(self):
        val = 50
        answer = 0
        for line in self.input:
            print(val, line, answer)
            dir = line[0]
            amount = int(line[1:])
            num_turns = amount // 100
            answer += num_turns
            amount = amount % 100
            if dir == "R":
                val += amount
                if val >= 100:
                    val %= 100
                    answer += 1
            elif dir == "L":
                if val == 0:
                    answer -= 1
                val -= amount
                if val < 0:
                    val %= 100
                    answer += 1
                if val == 0:
                    answer += 1
            print(val, line, answer)

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
