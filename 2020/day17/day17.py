with open("input", "r") as f:
    lines = [l.strip() for l in f.readlines()]

from itertools import product

import numpy as np

deltas = list(product([-1, 0, 1], repeat=3))
deltas.remove((0, 0, 0))
print(len(deltas))

num_cycles = 6
init_size = len(lines[0])
init_slice = np.zeros(shape=(len(lines[0]), len(lines[0])))
for i, line in enumerate(lines):
    for j, chr in enumerate(line):
        init_slice[i, j] = 1 if chr == "#" else 0
init_slice = np.pad(init_slice, num_cycles, constant_values=0)
print(init_slice.shape)

big_mat = np.zeros(
    shape=(init_size + 2 * num_cycles, init_size + 2 * num_cycles, 1 + 2 * num_cycles)
)
big_mat[:, :, num_cycles] = init_slice


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


for cycle in range(num_cycles):
    big_mat = update(big_mat)

print(f"Part 1: {np.sum(big_mat.flatten())}")


deltas = list(product([-1, 0, 1], repeat=4))
deltas.remove((0, 0, 0, 0))
print(len(deltas))

num_cycles = 6
init_size = len(lines[0])
init_slice = np.zeros(shape=(len(lines[0]), len(lines[0])))
for i, line in enumerate(lines):
    for j, chr in enumerate(line):
        init_slice[i, j] = 1 if chr == "#" else 0
init_slice = np.pad(init_slice, num_cycles, constant_values=0)
print(init_slice.shape)

big_mat = np.zeros(
    shape=(
        init_size + 2 * num_cycles,
        init_size + 2 * num_cycles,
        1 + 2 * num_cycles,
        1 + 2 * num_cycles,
    )
)
big_mat[:, :, num_cycles, num_cycles] = init_slice


def get_actives_4d(mat, x, y, z, w):
    num_actives = 0
    for d in deltas:
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


for cycle in range(num_cycles):
    big_mat = update_4d(big_mat)

print(f"Part 2: {np.sum(big_mat.flatten())}")
