from pathlib import Path

from aoc_utils import *

INPUT_FILE = Path(__file__).parent / "input"


class Solution:
    def __init__(self):
        self.input = read_input(INPUT_FILE)

    def solve_part_1(self):
        ranges = self.input[0].split(",")
        answer = 0
        for r in ranges:
            start, end = map(int, r.split("-"))
            for num in range(start, end + 1):
                if len(str(num)) % 2 == 0:
                    if str(num)[: len(str(num)) // 2] == str(num)[len(str(num)) // 2 :]:
                        answer += num
        print(answer)
        return answer

    def solve_part_2(self):
        ranges = self.input[0].split(",")
        answer = 0
        for r in ranges:
            ids = set()
            start, end = map(int, r.split("-"))
            for num in range(start, end + 1):
                s = len(str(num))
                for d in range(1, s // 2 + 1):
                    if (
                        len(str(num)) % d == 0
                        and str(num) == str(num)[:d] * (s // d)
                        and num not in ids
                    ):
                        ids.add(num)
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
