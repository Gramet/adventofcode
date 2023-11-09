from pathlib import Path


def advance(line, pos=0, right=3):
    pos = (pos + right) % 31
    is_tree = True if line[pos] == "#" else False

    if is_tree:
        return 1, pos
    else:
        return 0, pos


def go_down(lines, down=1, right=3):
    count = 0
    pos = 0
    for num_line, line in enumerate(lines):
        if num_line % down != 0 or num_line == 0:
            continue
        s = line
        hit_tree, pos = advance(s, pos, right)
        count += hit_tree

    return count


class Solution:
    def __init__(self):
        with open(Path(__file__).parent / "input", "r") as f:
            self.input = f.readlines()

    def solve_part_1(self):
        answer = go_down(self.input, 1, 3)
        print(answer)
        return answer

    def solve_part_2(self):
        answer = go_down(self.input, 1, 1)
        answer *= go_down(self.input, 1, 3)
        answer *= go_down(self.input, 1, 5)
        answer *= go_down(self.input, 1, 7)
        answer *= go_down(self.input, 2, 1)
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
