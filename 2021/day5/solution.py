from collections import defaultdict
from math import copysign
from pathlib import Path


class Solution:
    def __init__(self):
        with open(Path(__file__).parent / "input", "r") as f:
            self.input = f.readlines()
        self.segments = []
        for line in self.input:
            line = line.strip("\n")
            start, stop = line.split(" -> ")
            start_x, start_y = start.split(",")
            stop_x, stop_y = stop.split(",")
            self.segments.append(
                ((int(start_x), int(start_y)), (int(stop_x), int(stop_y)))
            )

    def solve_part_1(self):
        map = defaultdict(int)
        for seg in self.segments:
            if seg[0][0] == seg[1][0]:
                step = -int(copysign(1, seg[0][1] - seg[1][1]))
                for y in range(seg[0][1], seg[1][1] + step, step):
                    map[(seg[0][0], y)] += 1
            elif seg[0][1] == seg[1][1]:
                step = -int(copysign(1, seg[0][0] - seg[1][0]))
                for x in range(seg[0][0], seg[1][0] + step, step):
                    map[(x, seg[0][1])] += 1
        answer = sum(v >= 2 for v in map.values())
        print(answer)
        return answer

    def solve_part_2(self):
        map = defaultdict(int)
        for seg in self.segments:
            if seg[0][0] == seg[1][0]:
                step = -int(copysign(1, seg[0][1] - seg[1][1]))
                for y in range(seg[0][1], seg[1][1] + step, step):
                    map[(seg[0][0], y)] += 1
            elif seg[0][1] == seg[1][1]:
                step = -int(copysign(1, seg[0][0] - seg[1][0]))
                for x in range(seg[0][0], seg[1][0] + step, step):
                    map[(x, seg[0][1])] += 1
            else:
                step_y = -int(copysign(1, seg[0][1] - seg[1][1]))
                step_x = -int(copysign(1, seg[0][0] - seg[1][0]))
                range_x = list(range(seg[0][0], seg[1][0] + step_x, step_x))
                range_y = list(range(seg[0][1], seg[1][1] + step_y, step_y))
                for x, y in zip(range_x, range_y):
                    map[x, y] += 1
        answer = sum(v >= 2 for v in map.values())
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
