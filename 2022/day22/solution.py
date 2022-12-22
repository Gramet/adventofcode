from pathlib import Path
from collections import defaultdict
import re

dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]


class Solution:
    def __init__(self):
        with open(Path(__file__).parent / "input", "r") as f:
            self.input = f.read()
        self.map, self.instructions = self.input.split("\n\n")
        self.map_coos = defaultdict(int)
        self.start = None
        self.max_col = 0
        self.max_row = len(self.map.split("\n")) - 1
        for row, line in enumerate(self.map.split("\n")):
            self.max_col = max(self.max_col, len(line) - 1)
            for col, char in enumerate(line):
                if self.start is None and char != " ":
                    self.start = (row, col)
                if char == " ":
                    continue
                if char == ".":
                    self.map_coos[(row, col)] = 1
                if char == "#":
                    self.map_coos[(row, col)] = 2

        self.directions = re.findall("[RL]", self.instructions)
        self.steps = [int(x) for x in re.findall("\d+", self.instructions)]

    def solve_part_1(self):
        self.pos = self.start
        self.dir_idx = 0
        self.dir = dirs[self.dir_idx]
        for i, step in enumerate(self.steps):
            for _ in range(step):
                next_pos = (self.pos[0] + self.dir[0], self.pos[1] + self.dir[1])
                if self.map_coos[next_pos] == 1:
                    self.pos = next_pos
                elif self.map_coos[next_pos] == 2:
                    break
                elif self.map_coos[next_pos] == 0:
                    match self.dir:
                        case (0, 1):
                            next_pos = (self.pos[0], 0)

                        case (1, 0):
                            next_pos = (0, self.pos[1])

                        case (0, -1):
                            next_pos = (self.pos[0], self.max_col)

                        case (-1, 0):
                            next_pos = (self.max_row, self.pos[1])
                    while not self.map_coos[next_pos]:
                        next_pos = (
                            next_pos[0] + self.dir[0],
                            next_pos[1] + self.dir[1],
                        )
                    if self.map_coos[next_pos] == 1:
                        self.pos = next_pos
                    else:
                        break
            try:
                if self.directions[i] == "R":
                    self.dir_idx += 1
                else:
                    self.dir_idx -= 1
                self.dir_idx = self.dir_idx % len(dirs)
                self.dir = dirs[self.dir_idx]
            except:
                pass
        answer = 1000 * (1 + self.pos[0]) + 4 * (1 + self.pos[1]) + self.dir_idx
        print(answer)
        return answer

    def solve_part_2(self):
        self.pos = self.start
        self.dir_idx = 0
        self.dir = dirs[self.dir_idx]
        for i, step in enumerate(self.steps):
            for _ in range(step):
                next_pos = (self.pos[0] + self.dir[0], self.pos[1] + self.dir[1])
                if self.map_coos[next_pos] == 1:
                    self.pos = next_pos
                elif self.map_coos[next_pos] == 2:
                    break
                elif self.map_coos[next_pos] == 0:
                    match self.dir:
                        case (0, 1):
                            if 0 <= next_pos[0] <= 49:  # C
                                next_pos = (149 - next_pos[0], 99)
                                next_dir = (0, -1)
                            elif 50 <= next_pos[0] <= 99:  # A
                                next_pos = (49, next_pos[0] + 50)
                                next_dir = (-1, 0)
                            elif 100 <= next_pos[0] <= 149:  # C
                                next_pos = (149 - next_pos[0], 149)
                                next_dir = (0, -1)
                            elif 150 <= next_pos[0]:  # D
                                next_pos = (149, next_pos[0] - 100)
                                next_dir = (-1, 0)

                        case (1, 0):
                            if 0 <= next_pos[1] <= 49:  # G
                                next_pos = (0, next_pos[1] + 100)
                                next_dir = (1, 0)
                            elif 50 <= next_pos[1] <= 99:  # D:
                                next_pos = (100 + next_pos[1], 49)
                                next_dir = (0, -1)
                            elif 100 <= next_pos[1]:  # A
                                next_pos = (next_pos[1] - 50, 99)
                                next_dir = (0, -1)

                        case (0, -1):
                            if 0 <= next_pos[0] <= 49:  # F
                                next_pos = (149 - next_pos[0], 0)
                                next_dir = (0, 1)
                            elif 50 <= next_pos[0] <= 99:  # B
                                next_pos = (100, next_pos[0] - 50)
                                next_dir = (1, 0)
                            elif 100 <= next_pos[0] <= 149:  # F
                                next_pos = (149 - next_pos[0], 50)
                                next_dir = (0, 1)
                            elif 150 <= next_pos[0]:  # E
                                next_pos = (0, next_pos[0] - 100)
                                next_dir = (1, 0)

                        case (-1, 0):
                            if 0 <= next_pos[1] <= 49:  # B
                                next_pos = (50 + next_pos[1], 50)
                                next_dir = (0, 1)
                            elif 50 <= next_pos[1] <= 99:  # E
                                next_pos = (100 + next_pos[1], 0)
                                next_dir = (0, 1)
                            elif 100 <= next_pos[1]:  # G
                                next_pos = (199, next_pos[1] - 100)
                                next_dir = (-1, 0)

                    if self.map_coos[next_pos] == 1:
                        self.pos = next_pos
                        self.dir = next_dir
                        self.dir_idx = dirs.index(self.dir)
                    else:
                        break
            try:
                if self.directions[i] == "R":
                    self.dir_idx += 1
                else:
                    self.dir_idx -= 1
                self.dir_idx = self.dir_idx % len(dirs)
                self.dir = dirs[self.dir_idx]
            except:
                pass
        answer = 1000 * (1 + self.pos[0]) + 4 * (1 + self.pos[1]) + self.dir_idx
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
