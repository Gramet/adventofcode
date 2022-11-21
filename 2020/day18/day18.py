import re

with open("input", "r") as f:
    lines = [l.strip().replace(" ", "") for l in f.readlines()]


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


s = 0
for l in lines:
    s += int(evaluate(l))

print(f"Part 1: {s}")


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


s = 0
for l in lines:
    s += int(evaluate_addfirst(l))

print(f"Part 2: {s}")
