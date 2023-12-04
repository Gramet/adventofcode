from pathlib import Path
from string import printable, punctuation

from aoc_utils import *

INPUT_FILE = Path(__file__).parent / "input"

symbols = punctuation.replace(".", "")


class Solution:
    def __init__(self):
        self.input = read_input(INPUT_FILE)
        self.map = ascii_image_to_map(self.input, chr_map={x: x for x in printable})
        print(self.map)

    def find_number(self, pos):
        delta_left = 1
        val = self.map[pos]
        self.counted.append(pos)
        while True:
            next_pos = (pos[0], pos[1] - delta_left)
            if next_pos in self.counted:
                return None
            if self.map.get(next_pos, ".").isdigit():
                val = self.map.get(next_pos, ".") + val
                delta_left += 1
                self.counted.append(next_pos)
            else:
                break
        delta_right = 1
        while True:
            next_pos = (pos[0], pos[1] + delta_right)
            if next_pos in self.counted:
                return None
            if self.map.get(next_pos, ".").isdigit():
                val = val + self.map.get(next_pos, ".")
                delta_right += 1
                self.counted.append(next_pos)
            else:
                break
        return int(val)

    def solve_part_1(self):
        self.counted = []
        answer = 0
        for pos, val in self.map.items():
            if val.isdigit():
                r, c = pos
                for delta in deltas8_2d:
                    adj_pos = (r + delta[0], c + delta[1])
                    if self.map.get(adj_pos, ".") in symbols:
                        num = self.find_number(pos)
                        if num:
                            answer += num

        print(answer)
        return answer

    def solve_part_2(self):
        answer = 0
        for pos, val in self.map.items():
            if val != "*":
                continue
            print(pos)
            r, c = pos
            self.counted = []
            gear_nums = []
            for delta in deltas8_2d:
                adj_pos = (r + delta[0], c + delta[1])
                if self.map.get(adj_pos, ".").isdigit():
                    num = self.find_number(adj_pos)
                    if num:
                        gear_nums.append(num)
            if len(gear_nums) == 2:
                answer += gear_nums[0] * gear_nums[1]
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
