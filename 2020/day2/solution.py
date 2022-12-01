from pathlib import Path


def is_valid_num(line):
    requirements = line.split()[0]
    min = int(requirements.split("-")[0])
    max = int(requirements.split("-")[1])
    char = line.split()[1][0]
    pwd = line.split()[2]

    count = pwd.count(char)
    if count >= min and count <= max:
        return True
    else:
        return False


def is_valid_pos(line):
    requirements = line.split()[0]
    pos1 = int(requirements.split("-")[0]) - 1
    pos2 = int(requirements.split("-")[1]) - 1
    char = line.split()[1][0]
    pwd = line.split()[2]

    if (pwd[pos1] == char) ^ (pwd[pos2] == char):
        return True
    else:
        return False


class Solution:
    def __init__(self):
        with open(Path(__file__).parent / "input", "r") as f:
            self.input = f.readlines()

    def solve_part_1(self):
        answer = sum(True if is_valid_num(s) else False for s in self.input)
        print(answer)
        return answer

    def solve_part_2(self):
        answer = sum(True if is_valid_pos(s) else False for s in self.input)
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
