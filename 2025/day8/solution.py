import math
from collections import Counter
from pathlib import Path

from aoc_utils import *

INPUT_FILE = Path(__file__).parent / "input"


class Solution:
    def __init__(self):
        self.input = read_input(INPUT_FILE)

        self.boxes = [Point3D(x=x, y=y, z=z) for x, y, z in map(parse_ints, self.input)]

    def solve_part_1(self):
        dist_mat = {
            tuple(sorted((b1, b2))): b1.euclidean_distance(b2)
            for i, b1 in enumerate(self.boxes)
            for b2 in self.boxes[i + 1 :]
        }
        circuits_map = {b: i for i, b in enumerate(self.boxes)}
        sorted_dist_mat = [
            (b1, b2)
            for b1, b2 in sorted(dist_mat.keys(), key=lambda x: dist_mat[x])
            if b1 != b2
        ]
        for b1, b2 in sorted_dist_mat[:1000]:
            boxes_in_circuit1 = [
                b for b, c in circuits_map.items() if c == circuits_map[b1]
            ]
            for b in boxes_in_circuit1:
                circuits_map[b] = circuits_map[b2]

        answer = math.prod(
            x[1] for x in Counter(circuits_map.values()).most_common((3))
        )

        print(answer)
        return answer

    def solve_part_2(self):
        dist_mat = {
            tuple(sorted((b1, b2))): b1.euclidean_distance(b2)
            for i, b1 in enumerate(self.boxes)
            for b2 in self.boxes[i + 1 :]
        }
        circuits_map = {b: i for i, b in enumerate(self.boxes)}
        sorted_dist_mat = [
            (b1, b2)
            for b1, b2 in sorted(dist_mat.keys(), key=lambda x: dist_mat[x])
            if b1 != b2
        ]
        i = 0
        while len(Counter(circuits_map.values())) > 1:
            b1, b2 = sorted_dist_mat[i]
            boxes_in_circuit1 = [
                b for b, c in circuits_map.items() if c == circuits_map[b1]
            ]
            for b in boxes_in_circuit1:
                circuits_map[b] = circuits_map[b2]
            i += 1

        answer = b1.x * b2.x
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
