from pathlib import Path

from aoc_utils import *

INPUT_FILE = Path(__file__).parent / "input"


class Solution:
    def __init__(self):
        self.input = read_input(INPUT_FILE)
        self.map = ascii_image_to_map((self.input))

        self.galaxy_coos = [coo for coo, val in self.map.items() if val == 1]
        img_dim = max(self.map.keys())
        self.empty_rows = []
        self.empty_cols = []
        for row in range(img_dim[0] + 1):
            if all(self.map[(row, i)] == 0 for i in range(img_dim[1] + 1)):
                self.empty_rows.append(row)

        for col in range(img_dim[1] + 1):
            if all(self.map[(i, col)] == 0 for i in range(img_dim[0] + 1)):
                self.empty_cols.append(col)

    def compute_galaxy_dist(self, gal_1, gal_2, empty_fill) -> int:
        dist = manhattan_distance(gal_1, gal_2)
        extra_row_steps = sum(
            empty_fill if (gal_1[0] < r < gal_2[0] or gal_1[0] > r > gal_2[0]) else 0
            for r in self.empty_rows
        )
        extra_col_steps = sum(
            empty_fill if gal_1[1] < c < gal_2[1] or gal_1[1] > c > gal_2[1] else 0
            for c in self.empty_cols
        )
        dist += extra_row_steps + extra_col_steps
        return dist

    def solve_part_1(self) -> int:
        answer = 0
        for i, gal_1 in enumerate(self.galaxy_coos):
            for gal_2 in self.galaxy_coos[i + 1 :]:
                dist = self.compute_galaxy_dist(gal_1, gal_2, 1)
                answer += dist

        print(answer)
        return answer

    def solve_part_2(self) -> int:
        answer = 0
        for i, gal_1 in enumerate(self.galaxy_coos):
            for gal_2 in self.galaxy_coos[i + 1 :]:
                dist = self.compute_galaxy_dist(gal_1, gal_2, 999999)
                answer += dist
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
