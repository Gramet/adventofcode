from pathlib import Path

from aoc_utils import *

INPUT_FILE = Path(__file__).parent / "input"


class Solution:
    def __init__(self):
        self.input = read_input_parts(INPUT_FILE)
        presents = self.input[:-1]
        self.presents = {}
        for i, present in enumerate(presents):
            pres = {}
            for l, line in enumerate(present.splitlines()[1:]):
                for c, char in enumerate(line):
                    pres[Point2D(l, c)] = 0 if char == "." else 1
            self.presents[i] = pres

        self.present_sizes = [
            sum(present.values()) for present in self.presents.values()
        ]

        self.areas = self.input[-1]

    def solve_part_1(self):
        num_not_possible = 0
        answer = 0
        for area in self.areas.splitlines():
            R, C, *gifts = parse_ints(area)
            print(R)
            print(C)
            print(gifts)
            available_area = R * C
            required_area = sum(g * s for g, s in zip(gifts, self.present_sizes))

            if required_area > available_area:
                num_not_possible += 1
                print("Not enough space!!")
                continue
            if available_area >= 9 * sum(gifts):
                print("More than enough space!")
                answer += 1

        print(num_not_possible)
        print(answer)
        return answer

    def solve_part_2(self):
        answer = "None"
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
