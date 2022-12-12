import re
from pathlib import Path


def has_exact_double_digit(num):
    pat1 = re.compile(r"(\d)\1{1}")
    pat2 = re.compile(r"(\d)\1{2}")
    it1 = [i for i in pat1.finditer(num)]
    it2 = [i for i in pat2.finditer(num)]
    if it1:
        for match1 in it1:
            part_of_3 = False
            for match2 in it2:
                if match2.span(0)[0] <= match1.span(0)[0] < match2.span(0)[1]:
                    part_of_3 = True
            if not part_of_3:
                return True
        return False
    else:
        return False


def has_double_digit(num):
    for d1, d2 in zip(num[:-1], num[1:]):
        if d1 == d2:
            return True
    return False


class Solution:
    def __init__(self):
        with open(Path(__file__).parent / "input", "r") as f:
            self.input = f.readlines()
            self.min_, self.max_ = (int(x) for x in self.input[0].split("-"))

    def solve_part_1(self):
        count_valid = 0
        for num in range(self.min_, self.max_):
            num = str(num)
            if num == "".join(sorted(num)) and has_double_digit(num):
                count_valid += 1
        answer = count_valid
        print(answer)
        return answer

    def solve_part_2(self):
        count_valid = 0
        for num in range(self.min_, self.max_):
            num = str(num)
            if num == "".join(sorted(num)) and has_exact_double_digit(num):
                count_valid += 1
        answer = count_valid
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
