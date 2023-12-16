import sys
from pathlib import Path

from aoc_utils import *

sys.setrecursionlimit(1000000)
INPUT_FILE = Path(__file__).parent / "input"


class Solution:
    def __init__(self):
        self.input = read_input(INPUT_FILE)
        self.chr_map = {".": 0, "\\": 1, "/": 2, "|": 3, "-": 4}
        self.map = ascii_image_to_map(self.input, self.chr_map)
        self.energy_map = {k: set() for k in self.map}
        self.map_dim = max(self.map)
        self.max_steps = 1000000

    def trace_ray(self, start_pos, dir, step=0):
        if start_pos not in self.energy_map:
            return
        if dir in self.energy_map[start_pos]:
            return
        self.energy_map[start_pos].add(dir)
        step += 1
        if step > self.max_steps:
            return
        match self.map[start_pos], dir:
            case 0, _:
                self.trace_ray(
                    (start_pos[0] + dir[0], start_pos[1] + dir[1]), dir, step
                )
            case 1, (1, 0):
                self.trace_ray((start_pos[0], start_pos[1] + 1), (0, 1), step)
            case 1, (-1, 0):
                self.trace_ray((start_pos[0], start_pos[1] - 1), (0, -1), step)
            case 1, (0, 1):
                self.trace_ray((start_pos[0] + 1, start_pos[1]), (1, 0), step)
            case 1, (0, -1):
                self.trace_ray((start_pos[0] - 1, start_pos[1]), (-1, 0), step)
            case 2, (1, 0):
                self.trace_ray((start_pos[0], start_pos[1] - 1), (0, -1), step)
            case 2, (-1, 0):
                self.trace_ray((start_pos[0], start_pos[1] + 1), (0, 1), step)
            case 2, (0, 1):
                self.trace_ray((start_pos[0] - 1, start_pos[1]), (-1, 0), step)
            case 2, (0, -1):
                self.trace_ray((start_pos[0] + 1, start_pos[1]), (1, 0), step)

            case 3, (1, 0):
                self.trace_ray((start_pos[0] + 1, start_pos[1]), (1, 0), step)
            case 3, (-1, 0):
                self.trace_ray((start_pos[0] - 1, start_pos[1]), (-1, 0), step)
            case 3, (0, 1):
                self.trace_ray((start_pos[0] + 1, start_pos[1]), (1, 0), step)
                self.trace_ray((start_pos[0] - 1, start_pos[1]), (-1, 0), step)
            case 3, (0, -1):
                self.trace_ray((start_pos[0] - 1, start_pos[1]), (-1, 0), step)
                self.trace_ray((start_pos[0] + 1, start_pos[1]), (1, 0), step)

            case 4, (1, 0):
                self.trace_ray((start_pos[0], start_pos[1] - 1), (0, -1), step)
                self.trace_ray((start_pos[0], start_pos[1] + 1), (0, 1), step)
            case 4, (-1, 0):
                self.trace_ray((start_pos[0], start_pos[1] - 1), (0, -1), step)
                self.trace_ray((start_pos[0], start_pos[1] + 1), (0, 1), step)
            case 4, (0, 1):
                self.trace_ray((start_pos[0], start_pos[1] + 1), (0, 1), step)
            case 4, (0, -1):
                self.trace_ray((start_pos[0], start_pos[1] - 1), (0, -1), step)

    def solve_part_1(self):
        self.trace_ray((0, 0), (0, 1), 0)
        answer = sum(len(v) > 0 for v in self.energy_map.values())
        print(answer)
        return answer

    def solve_part_2(self):
        answer = 0
        for r in range(self.map_dim[0]):
            self.energy_map = {k: set() for k in self.map}
            self.trace_ray((r, 0), (0, 1))
            res = sum(len(v) > 0 for v in self.energy_map.values())
            answer = max(answer, res)
            self.energy_map = {k: set() for k in self.map}
            self.trace_ray((r, self.map_dim[1]), (0, -1))
            res = sum(len(v) > 0 for v in self.energy_map.values())
            answer = max(answer, res)
        for c in range(self.map_dim[1]):
            self.energy_map = {k: set() for k in self.map}
            self.trace_ray((0, c), (1, 0))
            res = sum(len(v) > 0 for v in self.energy_map.values())
            answer = max(answer, res)
            self.energy_map = {k: set() for k in self.map}
            self.trace_ray((self.map_dim[0], c), (-1, 0))
            res = sum(len(v) > 0 for v in self.energy_map.values())
            answer = max(answer, res)
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
