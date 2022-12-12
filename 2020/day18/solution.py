import re
from pathlib import Path


def evaluate(expr):
    while "(" in expr:
        start = 0
        end = 0
        for i, chr in enumerate(expr):
            if chr == "(":
                start = i
            elif chr == ")":
                end = i
                break
        expr = expr[:start] + evaluate(expr[start + 1 : end]) + expr[end + 1 :]

    nums = re.split("\+|\*", expr)
    ops = re.split("\d+", expr)[1:-1]
    res = int(nums[0])
    for num, op in zip(nums[1:], ops):
        if op == "+":
            res += int(num)
        elif op == "*":
            res *= int(num)

    return str(res)


def evaluate_addfirst(expr):
    while "(" in expr:
        start = 0
        end = 0
        for i, chr in enumerate(expr):
            if chr == "(":
                start = i
            elif chr == ")":
                end = i
                break
        expr = expr[:start] + evaluate_addfirst(expr[start + 1 : end]) + expr[end + 1 :]

    if "+" in expr and "*" in expr:
        l = expr.split("*")
        expr = "*".join(evaluate_addfirst(x) for x in l)

    nums = re.split("\+|\*", expr)
    ops = re.split("\d+", expr)[1:-1]
    res = int(nums[0])
    for num, op in zip(nums[1:], ops):
        if op == "+":
            res += int(num)
        elif op == "*":
            res *= int(num)

    return str(res)


class Solution:
    def __init__(self):
        with open(Path(__file__).parent / "input", "r") as f:
            self.input = [l.strip().replace(" ", "") for l in f.readlines()]

    def solve_part_1(self):
        answer = 0
        for l in self.input:
            answer += int(evaluate(l))
        print(answer)
        return answer

    def solve_part_2(self):
        answer = 0
        for l in self.input:
            answer += int(evaluate_addfirst(l))
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
