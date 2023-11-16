import re
from pathlib import Path

import numpy as np

from aoc_utils import read_input

INPUT_FILE = Path(__file__).parent / "input"


def intersection(cube1, cube2):
    # -cube2[0] because we will want to remove the intersections from counting
    cube_intersection = (
        -cube2[0],
        max(cube1[1], cube2[1]),
        min(cube1[2], cube2[2]),
        max(cube1[3], cube2[3]),
        min(cube1[4], cube2[4]),
        max(cube1[5], cube2[5]),
        min(cube1[6], cube2[6]),
    )
    if (
        cube_intersection[1] > cube_intersection[2]
        or cube_intersection[3] > cube_intersection[4]
        or cube_intersection[5] > cube_intersection[6]
    ):
        return None
    return cube_intersection


class Solution:
    def __init__(self):
        self.input = read_input(INPUT_FILE)
        self.cube_size = 101
        self.cube = np.zeros((self.cube_size, self.cube_size, self.cube_size))
        self.offset = (self.cube_size - 1) // 2

    def solve_part_1(self):
        for line in self.input:
            val = 1 if line.startswith("on") else 0
            start_x, end_x, start_y, end_y, start_z, end_z = [
                max(min(int(x), self.offset + 1), -self.offset - 1) + self.offset
                for x in re.findall(r"-?\d+", line)
            ]
            self.cube[
                start_x : end_x + 1, start_y : end_y + 1, start_z : end_z + 1
            ] = val

        answer = int(self.cube.sum(axis=None))
        print(answer)
        return answer

    def solve_part_2(self):
        cubes = []
        for line in self.input:
            val = 1 if line.startswith("on") else -1
            start_x, end_x, start_y, end_y, start_z, end_z = [
                int(x) for x in re.findall(r"-?\d+", line)
            ]
            cubes.append((val, start_x, end_x, start_y, end_y, start_z, end_z))

        counted_cubes = []
        for cube in cubes:
            to_turn_on = [cube] if cube[0] == 1 else []
            for counted_cube in counted_cubes:
                intersect = intersection(cube, counted_cube)
                if intersect is not None:
                    to_turn_on.append(intersect)
            counted_cubes += to_turn_on

        answer = 0
        for cube in counted_cubes:
            answer += (
                cube[0]
                * (cube[2] - cube[1] + 1)
                * (cube[4] - cube[3] + 1)
                * (cube[6] - cube[5] + 1)
            )

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
