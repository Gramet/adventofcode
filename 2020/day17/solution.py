from pathlib import Path
from itertools import product

import numpy as np

deltas = list(product([-1, 0, 1], repeat=3))
deltas.remove((0, 0, 0))

deltas4d = list(product([-1, 0, 1], repeat=4))
deltas4d.remove((0, 0, 0, 0))


def get_actives(mat, x, y, z):
    num_actives = 0
    for d in deltas:
        if (
            0 <= x + d[0] < mat.shape[0]
            and 0 <= y + d[1] < mat.shape[1]
            and 0 <= z + d[2] < mat.shape[2]
        ):
            num_actives += mat[x + d[0], y + d[1], z + d[2]]

    return num_actives


def update(mat):
    new_mat = mat.copy()
    for z in range(mat.shape[2]):
        for y in range(mat.shape[1]):
            for x in range(mat.shape[0]):
                num_actives = get_actives(mat, x, y, z)
                if mat[x, y, z] == 0 and num_actives == 3:
                    new_mat[x, y, z] = 1
                elif mat[x, y, z] == 1 and (num_actives > 3 or num_actives < 2):
                    new_mat[x, y, z] = 0

    return new_mat


def get_actives_4d(mat, x, y, z, w):
    num_actives = 0
    for d in deltas4d:
        if (
            0 <= x + d[0] < mat.shape[0]
            and 0 <= y + d[1] < mat.shape[1]
            and 0 <= z + d[2] < mat.shape[2]
            and 0 <= w + d[3] < mat.shape[3]
        ):
            num_actives += mat[x + d[0], y + d[1], z + d[2], w + d[3]]

    return num_actives


def update_4d(mat):
    new_mat = mat.copy()
    for w in range(mat.shape[3]):
        for z in range(mat.shape[2]):
            for y in range(mat.shape[1]):
                for x in range(mat.shape[0]):
                    num_actives = get_actives_4d(mat, x, y, z, w)
                    if mat[x, y, z, w] == 0 and num_actives == 3:
                        new_mat[x, y, z, w] = 1
                    elif mat[x, y, z, w] == 1 and (num_actives > 3 or num_actives < 2):
                        new_mat[x, y, z, w] = 0

    return new_mat


class Solution:
    def __init__(self):
        with open(Path(__file__).parent / "input", "r") as f:
            self.input = [l.strip() for l in f.readlines()]

        self.num_cycles = 6
        init_size = len(self.input[0])
        init_slice = np.zeros(shape=(len(self.input[0]), len(self.input[0])))
        for i, line in enumerate(self.input):
            for j, chr in enumerate(line):
                init_slice[i, j] = 1 if chr == "#" else 0
        init_slice = np.pad(init_slice, self.num_cycles, constant_values=0)

        self.big_mat = np.zeros(
            shape=(
                init_size + 2 * self.num_cycles,
                init_size + 2 * self.num_cycles,
                1 + 2 * self.num_cycles,
            )
        )
        self.big_mat[:, :, self.num_cycles] = init_slice

        self.big_mat4d = np.zeros(
            shape=(
                init_size + 2 * self.num_cycles,
                init_size + 2 * self.num_cycles,
                1 + 2 * self.num_cycles,
                1 + 2 * self.num_cycles,
            )
        )
        self.big_mat4d[:, :, self.num_cycles, self.num_cycles] = init_slice

    def solve_part_1(self):
        for _ in range(self.num_cycles):
            self.big_mat = update(self.big_mat)

        answer = int(np.sum(self.big_mat.flatten()))
        print(answer)
        return answer

    def solve_part_2(self):
        for _ in range(self.num_cycles):
            self.big_mat4d = update_4d(self.big_mat4d)
        answer = int(np.sum(self.big_mat4d.flatten()))
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
