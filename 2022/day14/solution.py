from pathlib import Path
from collections import defaultdict
from math import copysign

sign = lambda x: copysign(1, x)


def point_to_tuple(point):
    point = point.split(",")
    return (int(point[0]), int(point[1]))


class Solution:
    def __init__(self):
        with open(Path(__file__).parent / "input", "r") as f:
            self.input = f.readlines()
        self.cave = defaultdict(int)
        for line in self.input:
            path = line.strip().split("->")
            start = point_to_tuple(path[0])
            self.cave[start] = 1
            prev = start
            for point in path[1:]:
                pos = point_to_tuple(point)
                self.cave[pos] = 1
                diff = (pos[0] - prev[0], pos[1] - prev[1])
                diff_x, diff_y = diff[0], diff[1]
                for dx in range(abs(diff_x) + 1):
                    self.cave[(int(prev[0] + dx * sign(diff_x)), prev[1])] = 1
                for dy in range(abs(diff_y) + 1):
                    self.cave[(prev[0], int(prev[1] + dy * sign(diff_y)))] = 1
                prev = pos
        self.max_depth = max(x[1] for x in self.cave.keys())
        self.floor = self.max_depth + 2

    def solve_part_1(self):
        sand_start = (500, 0)
        finished = False
        self.num_sand = 0
        while not finished:
            pos = sand_start
            while True:
                if not self.cave[(pos[0], pos[1] + 1)]:
                    pos = (pos[0], pos[1] + 1)
                elif not self.cave[(pos[0] - 1, pos[1] + 1)]:
                    pos = (pos[0] - 1, pos[1] + 1)
                elif not self.cave[(pos[0] + 1, pos[1] + 1)]:
                    pos = (pos[0] + 1, pos[1] + 1)
                else:
                    self.cave[pos] = 2
                    self.num_sand += 1
                    break
                if pos[1] >= self.max_depth:
                    finished = True
                    break
        answer = self.num_sand
        print(answer)
        return answer

    def solve_part_2(self):
        sand_start = (500, 0)
        finished = False
        while not finished:
            pos = sand_start
            while True:
                if pos[1] + 1 == self.floor:
                    self.cave[pos] = 2
                    self.num_sand += 1
                    break
                if not self.cave[(pos[0], pos[1] + 1)]:
                    pos = (pos[0], pos[1] + 1)
                elif not self.cave[(pos[0] - 1, pos[1] + 1)]:
                    pos = (pos[0] - 1, pos[1] + 1)
                elif not self.cave[(pos[0] + 1, pos[1] + 1)]:
                    pos = (pos[0] + 1, pos[1] + 1)
                elif pos == (500, 0):
                    self.num_sand += 1
                    finished = True
                    break
                else:
                    self.cave[pos] = 2
                    self.num_sand += 1
                    break

        answer = self.num_sand
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
