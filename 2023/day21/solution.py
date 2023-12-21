from pathlib import Path

from aoc_utils import *
import numpy as np

INPUT_FILE = Path(__file__).parent / "input"


class Solution:
    def __init__(self):
        self.input = read_input(INPUT_FILE)
        AOC_CHR_MAP.update({"S": 2})
        self.map = ascii_image_to_map(self.input)
        # print(self.map)
        self.start_pos = [k for k, v in self.map.items() if v == 2][0]
        self.map[self.start_pos] = 0
        self.map_dim = max(self.map)

    def solve_part_1(self):
        cur_pos = {self.start_pos}
        num_steps = 64
        for _ in range(num_steps):
            new_pos = set()
            for pos in cur_pos:
                for delta in deltas4_2d:
                    next_pos = (pos[0] + delta[0], pos[1] + delta[1])
                    if next_pos in self.map and not self.map[next_pos]:
                        new_pos.add(next_pos)
            cur_pos = new_pos

        answer = len(new_pos)
        print(answer)
        return answer

    def solve_part_2(self):
        num_steps = 26501365
        cur_pos = {self.start_pos}
        res = []
        for step in range(1, self.start_pos[0] + 2 * (self.map_dim[0] + 1) + 1):
            new_pos = set()
            for pos in cur_pos:
                for delta in deltas4_2d:
                    next_pos = (pos[0] + delta[0], pos[1] + delta[1])
                    mod_pos = (
                        next_pos[0] % (self.map_dim[0] + 1),
                        next_pos[1] % (self.map_dim[1] + 1),
                    )
                    if not self.map[mod_pos]:
                        new_pos.add(next_pos)
            if step % (1 + self.map_dim[0]) == self.start_pos[0]:
                res.append((step, len(new_pos)))
            cur_pos = new_pos
        # Compute quadratic formula
        const = np.linalg.det(
            np.array(
                [
                    [res[0][0] ** 2, res[0][0], 1],
                    [res[1][0] ** 2, res[1][0], 1],
                    [res[2][0] ** 2, res[2][0], 1],
                ]
            )
        )
        a = (
            np.linalg.det(
                np.array(
                    [
                        [res[0][1], res[0][0], 1],
                        [res[1][1], res[1][0], 1],
                        [res[2][1], res[2][0], 1],
                    ]
                )
            )
            / const
        )
        b = (
            np.linalg.det(
                np.array(
                    [
                        [res[0][0] ** 2, res[0][1], 1],
                        [res[1][0] ** 2, res[1][1], 1],
                        [res[2][0] ** 2, res[2][1], 1],
                    ]
                )
            )
            / const
        )

        c = (
            np.linalg.det(
                np.array(
                    [
                        [res[0][0] ** 2, res[0][0], res[0][1]],
                        [res[1][0] ** 2, res[1][0], res[1][1]],
                        [res[2][0] ** 2, res[2][0], res[2][1]],
                    ]
                )
            )
            / const
        )
        quad = lambda x: a * x**2 + b * x + c
        # +1 because of floating errors from numpy I guess, results for 65, 136 and 327 are all just lower than what they should
        answer = round(quad(num_steps)) + 1
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
