from itertools import chain
from pathlib import Path

import tqdm

from aoc_utils import *

INPUT_FILE = Path(__file__).parent / "input"

RED = 1
GREEN = 2
BLUE = 3
OUTSIDE = -1


class Solution:
    def __init__(self):
        self.input = read_input(INPUT_FILE)
        self.coos = [Point2D(x, y) for x, y in map(parse_ints, self.input)]

    def solve_part_1(self):
        max_area = 0
        for coo in self.coos:
            for coo2 in self.coos:
                if coo != coo2:
                    area = (abs(coo.x - coo2.x) + 1) * (abs(coo.y - coo2.y) + 1)
                    max_area = max(max_area, area)
        answer = max_area
        print(answer)
        return answer

    def check_in_loop(self, point):
        xs = sorted({p.x for p in self.borders[point.y] if p.x >= point.x})

        segments = 0
        prev = None
        for x in xs:
            if prev is None or x != prev + 1:
                segments += 1
                prev = x
            elif x == prev + 1:
                prev = x
        return segments % 2 == 1

    def solve_part_2(self):
        self.map = defaultdict(int)
        self.borders = dict()
        # Fill in green areas
        for i, coo in enumerate(self.coos[:-1]):
            coo2 = self.coos[i + 1]
            for x in range(min(coo.x, coo2.x), max(coo.x, coo2.x) + 1):
                for y in range(min(coo.y, coo2.y), max(coo.y, coo2.y) + 1):
                    self.map[Point2D(x, y)] = GREEN
                    self.borders.setdefault(y, set()).add(Point2D(x, y))

        # Fill last border
        for x in range(
            min(self.coos[-1].x, self.coos[0].x),
            max(self.coos[-1].x, self.coos[0].x) + 1,
        ):
            for y in range(
                min(self.coos[-1].y, self.coos[0].y),
                max(self.coos[-1].y, self.coos[0].y) + 1,
            ):
                self.map[Point2D(x, y)] = GREEN
                self.borders.setdefault(y, set()).add(Point2D(x, y))

        rect_areas = {}
        for i, coo in enumerate(self.coos):
            for coo2 in self.coos[: i + 1]:
                area = (abs(coo.x - coo2.x) + 1) * (abs(coo.y - coo2.y) + 1)
                rect_areas[(coo, coo2)] = area

        # print_2d_image(self.map, int_map={0: ".", GREEN: "X", BLUE: "B", RED: "#"})

        for rect, area in tqdm.tqdm(
            sorted(rect_areas.items(), key=lambda x: x[1], reverse=True)
        ):
            coo, coo2 = rect
            rect_border_coos = chain(
                (
                    Point2D(coo.x, y)
                    for y in range(min(coo.y, coo2.y), max(coo.y, coo2.y) + 1)
                ),
                (
                    Point2D(coo2.x, y)
                    for y in range(min(coo.y, coo2.y), max(coo.y, coo2.y) + 1)
                ),
                (
                    Point2D(x, coo2.y)
                    for x in range(min(coo.x, coo2.x), max(coo.x, coo2.x) + 1)
                ),
                (
                    Point2D(x, coo.y)
                    for x in range(min(coo.x, coo2.x), max(coo.x, coo2.x) + 1)
                ),
            )

            valid = True
            for point in rect_border_coos:
                if self.map[point] == OUTSIDE:
                    valid = False
                    break
                if self.map[point] == 0:
                    if not self.check_in_loop(point):
                        self.map[point] = OUTSIDE
                        valid = False
                        break
                    else:
                        self.map[point] = BLUE
                if not valid:
                    break

            if valid:
                answer = area
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
