from copy import deepcopy
from pathlib import Path

from aoc_utils import read_input

INPUT_FILE = Path(__file__).parent / "input"


class Solution:
    def __init__(self):
        self.input = read_input(INPUT_FILE)

        self.map = {}
        for r, line in enumerate(self.input):
            for c, char in enumerate(line.strip()):
                self.map[(r, c)] = char

    def solve_part_1(self):
        cur_map = self.map
        change = True
        steps = 0
        while change:
            next_map = deepcopy(cur_map)
            # move right
            change = False
            steps += 1
            for pos, val in cur_map.items():
                right_square = (pos[0], pos[1] + 1)
                if right_square not in cur_map:
                    right_square = (pos[0], 0)
                if val == ">" and cur_map.get(right_square, "X") == ".":
                    next_map[pos] = "."
                    next_map[right_square] = ">"
                    change = True
            # move down
            temp_map = next_map
            next_map = deepcopy(temp_map)
            for pos, val in temp_map.items():
                down_square = (pos[0] + 1, pos[1])
                if down_square not in temp_map:
                    down_square = (0, pos[1])
                if val == "v" and temp_map.get(down_square, "X") == ".":
                    next_map[pos] = "."
                    next_map[down_square] = "v"
                    change = True
            cur_map = next_map
        answer = steps
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
