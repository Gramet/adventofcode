from collections import Counter
from os import close
from pathlib import Path

from aoc_utils import *

INPUT_FILE = Path(__file__).parent / "input"


class Solution:
    def __init__(self):
        self.input = read_input(INPUT_FILE)
        self.coos = [parse_ints(x) for x in self.input]
        self.min_x = min([coo[0] for coo in self.coos])
        self.min_y = min([coo[1] for coo in self.coos])
        self.max_x = max([coo[0] for coo in self.coos])
        self.max_y = max([coo[1] for coo in self.coos])

    def solve_part_1(self):
        closest = {}
        for x in range(self.min_x, self.max_x + 1):
            for y in range(self.min_y, self.max_y + 1):
                dists = {}
                for idx, coo in enumerate(self.coos):
                    distance = manhattan_distance(coo, (x, y))
                    dists[distance] = dists.get(distance, []) + [idx]
                if len(dists[min(dists)]) == 1:
                    closest[(x, y)] = dists[min(dists)][0]

        to_ignore = set(
            [
                val
                for key, val in closest.items()
                if key[0] == self.min_x
                or key[0] == self.max_x
                or key[1] == self.min_y
                or key[1] == self.max_y
            ]
        )
        area_size = Counter(closest.values())
        for key in to_ignore:
            del area_size[key]

        answer = max(area_size.values())
        print(answer)
        return answer

    def solve_part_2(self):
        points = []
        for x in range(self.min_x, self.max_x + 1):
            for y in range(self.min_y, self.max_y + 1):
                dist = 0
                for idx, coo in enumerate(self.coos):
                    dist += manhattan_distance(coo, (x, y))

                if dist < 10000:
                    points.append(coo)
        answer = len(points)
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
