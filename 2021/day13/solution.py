from pathlib import Path
import numpy as np


class Solution:
    def __init__(self):
        with open(Path(__file__).parent / "input", "r") as f:
            self.input = f.read()
            self.coos, self.folds = self.input.split("\n\n")
        x, y = self.coos.split("\n")[0].strip("\n").split(",")
        list_coos = []
        for line in self.coos.split("\n"):
            x, y = line.strip("\n").split(",")
            list_coos.append((int(x), int(y)))
        self.map = np.zeros(
            shape=(
                max(list_coos, key=lambda x: x[0])[0] + 1,
                max(list_coos, key=lambda x: x[1])[1] + 1,
            )
        )
        for x, y in list_coos:
            self.map[x, y] += 1
        self.list_folds = []
        for fold in self.folds.split("\n")[:-1]:
            dir, val = fold.split("=")
            self.list_folds.append((dir[-1], int(val)))
        print(self.list_folds)

    def solve_part_1(self):
        for dir, val in self.list_folds:
            if dir == "y":
                self.map = self.map[:, :val] + np.fliplr(self.map[:, val + 1 :])
            else:
                self.map = self.map[:val, :] + np.flipud(self.map[val + 1 :, :])
            break
        answer = (self.map > 0).sum()

        print(answer)
        return answer

    def solve_part_2(self):
        for dir, val in self.list_folds[1:]:
            if dir == "y":
                self.map = self.map[:, :val] + np.fliplr(self.map[:, val + 1 :])
            else:
                self.map = self.map[:val, :] + np.flipud(self.map[val + 1 :, :])
        map_str = ""
        for row in self.map.T:
            for val in row:
                if val > 0:
                    map_str += "#"
                else:
                    map_str += "."
            map_str += "\n"
        print(map_str)
        answer = "AHGCPGAU"
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
