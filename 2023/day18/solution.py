from pathlib import Path

from aoc_utils import *


INPUT_FILE = Path(__file__).parent / "input"


class Solution:
    def __init__(self):
        self.input = read_input(INPUT_FILE)

    def solve_part_1(self):
        pos = (0, 0)
        self.dir_map = {"R": (0, 1), "L": (0, -1), "D": (1, 0), "U": (-1, 0)}
        self.curve = []
        num_points = 0
        for line in self.input:
            dir, length, color = line.strip().split()
            delta = self.dir_map[dir]
            pos = (pos[0] + delta[0] * int(length), pos[1] + delta[1] * int(length))
            self.curve.append(pos)
            num_points += int(length)

        answer = curve_area(self.curve, num_points)

        print(answer)
        return answer

    def solve_part_2(self):
        pos = (0, 0)
        self.dir_map = {"0": (0, 1), "2": (0, -1), "1": (1, 0), "3": (-1, 0)}
        self.curve = []
        num_points = 0
        for line in self.input:
            _, _, color = line.strip().split()
            length, dir = int(color[2:7], 16), color[7:8]
            delta = self.dir_map[dir]
            pos = (pos[0] + delta[0] * length, pos[1] + delta[1] * length)
            self.curve.append(pos)
            num_points += length

        answer = curve_area(self.curve, num_points)

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
