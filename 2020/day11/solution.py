from copy import deepcopy
from itertools import product
from pathlib import Path

dict_seat = {".": -1, "L": 0, "#": 1}

dirs = list(product([-1, 0, 1], repeat=2))
dirs.remove((0, 0))


def change_seats(mat):
    mat_cop = deepcopy(mat)
    for row in range(1, len(mat) - 1):
        for col in range(1, len(mat[row]) - 1):
            num_neigh = 0
            for dir in dirs:
                dir_x, dir_y = dir
                num_neigh += int(mat_cop[row + dir_x][col + dir_y] > 0)

            if mat_cop[row][col] == 0 and num_neigh == 0:
                mat[row][col] = 1
            elif mat_cop[row][col] == 1 and num_neigh >= 4:
                mat[row][col] = 0

    return mat


def find_nearest(mat, row, col, dir_row, dir_col):
    dir_row_ori = dir_row
    dir_col_ori = dir_col
    while True:
        if (
            row + dir_row == len(mat)
            or row + dir_row == -1
            or col + dir_col == len(mat[row])
            or col + dir_col == -1
        ):
            return 0
        if mat[row + dir_row][col + dir_col] == -1:
            dir_row += dir_row_ori
            dir_col += dir_col_ori
        else:
            return mat[row + dir_row][col + dir_col]


def change_seats_far(mat):
    mat_cop = deepcopy(mat)
    for row in range(1, len(mat) - 1):
        for col in range(1, len(mat[row]) - 1):
            num_neigh = 0
            for dir in dirs:
                dir_x, dir_y = dir
                num_neigh += find_nearest(mat_cop, row, col, dir_x, dir_y)

            if mat_cop[row][col] == 0 and num_neigh == 0:
                mat[row][col] = 1
            elif mat_cop[row][col] == 1 and num_neigh >= 5:
                mat[row][col] = 0

    return mat


class Solution:
    def __init__(self):
        with open(Path(__file__).parent / "input", "r") as f:
            self.input = f.readlines()
        self.mat = [[-1] * (len(self.input[0].strip("\n")) + 2)]

        for line in self.input:
            self.mat.append([-1] + [dict_seat[x] for x in line.strip("\n")] + [-1])
        self.mat.append([-1] * (len(self.input[0].strip("\n")) + 2))

        self.num_floor = -sum(sum(row) for row in self.mat)
        self.mat2 = deepcopy(self.mat)

    def solve_part_1(self):
        while True:
            if self.mat == change_seats(deepcopy(self.mat)):
                break
            else:
                self.mat = change_seats(deepcopy(self.mat))
        answer = sum(sum(row) for row in self.mat) + self.num_floor
        print(answer)
        return answer

    def solve_part_2(self):
        while True:
            if self.mat2 == change_seats_far(deepcopy(self.mat2)):
                break
            else:
                self.mat2 = change_seats_far(deepcopy(self.mat2))
        answer = sum(sum(row) for row in self.mat2) + self.num_floor
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
