from pathlib import Path

from aoc_utils import *

INPUT_FILE = Path(__file__).parent / "input"


class Solution:
    def __init__(self):
        ranges, ids = read_input_parts(INPUT_FILE)
        self.ids = parse_ints(ids)
        self.ranges = [list(map(int, r.split("-"))) for r in ranges.split("\n")]

    def solve_part_1(self):
        answer = 0
        for id in self.ids:
            for start, end in self.ranges:
                if start <= id <= end:
                    answer += 1
                    break
        print(answer)
        return answer

    def solve_part_2(self):
        answer = 0
        checked_ranges = []
        for r in sorted(self.ranges, key=lambda x: x[0]):
            ori_r = r.copy()
            for checked_r in checked_ranges:
                if checked_r[0] <= r[0] <= checked_r[1]:
                    r[0] = checked_r[1] + 1
                if checked_r[0] <= r[1] <= checked_r[1]:
                    r[1] = checked_r[0] - 1

            if r[0] > r[1]:
                continue
            answer += r[1] - r[0] + 1
            checked_ranges.append(ori_r)
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
