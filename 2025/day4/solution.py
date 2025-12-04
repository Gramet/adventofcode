from pathlib import Path

from aoc_utils import *

INPUT_FILE = Path(__file__).parent / "input"


class Solution:
    def __init__(self):
        self.input = read_input(INPUT_FILE)
        self.map = ascii_image_to_map(self.input, {".": 0, "@": 1})

    def solve_part_1(self):
        answer = 0
        for point, val in self.map.copy().items():
            if val == 0:
                continue
            num_neigh = sum(
                self.map[neighbor] for neighbor in point.neighbours(deltas8_2d)
            )
            if num_neigh < 4:
                answer += 1

        print(answer)
        return answer

    def solve_part_2(self):
        answer = 0
        while True:
            new_map = self.map.copy()
            for point, val in self.map.copy().items():
                if val == 0:
                    continue
                num_neigh = sum(
                    self.map[neighbor] for neighbor in point.neighbours(deltas8_2d)
                )
                if num_neigh < 4:
                    new_map[point] = 0
                    answer += 1
            if new_map == self.map:
                break
            self.map = new_map
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
