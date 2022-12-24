import sys
from collections import defaultdict
from copy import deepcopy
from pathlib import Path

# sys.setrecursionlimit(10000)

deltas = [(1, 0), (0, 1), (0, -1), (-1, 0), (0, 0)]


def manhattan(start, end):
    return abs(start[0] - end[0]) + abs(start[1] - end[1])


class Solution:
    def __init__(self):
        with open(Path(__file__).parent / "input", "r") as f:
            self.input = f.readlines()
        self.map = defaultdict(int)
        self.blizzards_up = {}
        self.blizzards_left = {}
        self.blizzards_right = {}
        self.blizzards_down = {}

        for row, line in enumerate(self.input):
            for col, char in enumerate(line.strip()):
                if row == 0 and char == ".":
                    self.start = (row, col)
                if row == len(self.input) - 1 and char == ".":
                    self.end = (row, col)
                if char == "#":
                    self.map[(row, col)] = -1
                elif char == "^":
                    self.map[(row, col)] = 1
                    self.blizzards_up[(row, col)] = (-1, 0)
                elif char == "<":
                    self.map[(row, col)] = 1
                    self.blizzards_left[(row, col)] = (0, -1)
                elif char == ">":
                    self.map[(row, col)] = 1
                    self.blizzards_right[(row, col)] = (0, 1)
                elif char == "v":
                    self.map[(row, col)] = 1
                    self.blizzards_down[(row, col)] = (1, 0)
        self.blizzards = [
            self.blizzards_down,
            self.blizzards_left,
            self.blizzards_right,
            self.blizzards_up,
        ]
        self.max_row = len(self.input) - 1
        self.max_col = len(line.strip()) - 1
        print(self.start, self.end)
        print(self.max_col, self.max_row)

    def next_blizzards(self, blizzards):
        new_blizzards = []
        for blizdir in blizzards:
            next_blizzards = {}
            for blizzard, dir in blizdir.items():
                new_blizzard = (blizzard[0] + dir[0], blizzard[1] + dir[1])
                if new_blizzard[0] == 0:
                    new_blizzard = (self.max_row - 1, new_blizzard[1])
                if new_blizzard[0] == self.max_row:
                    new_blizzard = (1, new_blizzard[1])
                if new_blizzard[1] == 0:
                    new_blizzard = (new_blizzard[0], self.max_col - 1)
                if new_blizzard[1] == self.max_col:
                    new_blizzard = (new_blizzard[0], 1)
                next_blizzards[new_blizzard] = dir
            new_blizzards.append(next_blizzards)
        return new_blizzards

    def is_valid(self, coo):
        return (
            (0 < coo[0] < self.max_row and 0 < coo[1] < self.max_col)
            or coo == self.start
            or coo == self.end
        )

    def find_path(self, pos, end, blizzards, time_spent):
        print(pos, time_spent)
        while True:
            time_spent += 1
            blizzards = self.next_blizzards(blizzards)
            new_safe_pos = []
            for p in pos:
                for delta in deltas:
                    new_p = (p[0] + delta[0], p[1] + delta[1])
                    if self.is_valid(new_p) and new_p not in set().union(*blizzards):
                        new_safe_pos.append(new_p)

            pos = set(new_safe_pos)

            if end in new_safe_pos:
                break
        return time_spent, blizzards

    def solve_part_1(self):
        blizzards = deepcopy(self.blizzards)
        start = {self.start}
        end = self.end
        self.best_time = 99999999999
        time_spent = 0

        answer, _ = self.find_path(start, end, blizzards, time_spent)
        print(answer)
        return answer

    def solve_part_2(self):
        blizzards = deepcopy(self.blizzards)
        start = self.start
        end = self.end
        self.best_time = 99999999999
        time_spent = 0

        time_spent, blizzards = self.find_path({start}, end, blizzards, time_spent)
        time_spent, blizzards = self.find_path({end}, start, blizzards, time_spent)
        answer, blizzards = self.find_path({start}, end, blizzards, time_spent)

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
