from pathlib import Path

from aoc_utils import *

INPUT_FILE = Path(__file__).parent / "input"


class Solution:
    def __init__(self):
        self.input = read_input_parts(INPUT_FILE)

        self.locks = []
        self.keys = []
        for part in self.input:
            if part[0] == "#":
                # Lock
                lock = part.splitlines()
                lock_height = [-1, -1, -1, -1, -1]
                for row in lock:
                    for col, chr in enumerate(row):
                        if chr == "#":
                            lock_height[col] += 1
                self.locks.append(lock_height)
            elif part[0] == ".":
                # key
                # Lock
                key = part.splitlines()
                key_height = [-1, -1, -1, -1, -1]
                for row in key:
                    for col, chr in enumerate(row):
                        if chr == "#":
                            key_height[col] += 1
                self.keys.append(key_height)

    def solve_part_1(self):
        def check(key, lock):
            for col in range(5):
                if key[col] + lock[col] > 5:
                    return False
            return True

        answer = 0
        for key in self.keys:
            for lock in self.locks:
                if check(key, lock):
                    answer += 1
        print(answer)
        return answer

    def solve_part_2(self):
        answer = "None"
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
