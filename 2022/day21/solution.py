from pathlib import Path
from copy import deepcopy
from math import copysign

sign = lambda x: copysign(1, x)


def op(monkey, monkey2, operator):
    match operator:
        case "+":
            return monkey + monkey2
        case "*":
            return monkey * monkey2
        case "-":
            return monkey - monkey2
        case "/":
            return monkey / monkey2
        case _:
            raise ValueError(f"Unsupported case {operator}")


def solve(monkeys):
    while isinstance(monkeys["root"], list):
        for monkey, job in monkeys.items():
            if isinstance(job, (int, float)):
                continue
            if isinstance(monkeys[job[0]], (int, float)) and isinstance(
                monkeys[job[2]], (int, float)
            ):
                monkeys[monkey] = op(monkeys[job[0]], monkeys[job[2]], job[1])
    return int(monkeys["root"])


class Solution:
    def __init__(self):
        with open(Path(__file__).parent / "input", "r") as f:
            self.input = f.readlines()

        self.monkeys = {}

        for line in self.input:
            monkey, job = line.split(":")
            try:
                job = int(job)
            except:
                job = job.strip().split(" ")
            self.monkeys[monkey] = job

    def solve_part_1(self):
        monkeys = deepcopy(self.monkeys)
        while isinstance(monkeys["root"], list):
            for monkey, job in monkeys.items():
                if isinstance(job, (int, float)):
                    continue
                if isinstance(monkeys[job[0]], (int, float)) and isinstance(
                    monkeys[job[2]], (int, float)
                ):
                    monkeys[monkey] = op(monkeys[job[0]], monkeys[job[2]], job[1])
        answer = int(monkeys["root"])
        print(answer)
        return answer

    def solve_part_2(self):
        self.monkeys = {}

        for line in self.input:
            monkey, job = line.split(":")
            try:
                job = int(job)
            except:
                job = job.strip().split(" ")
            self.monkeys[monkey] = job

        self.monkeys["root"][1] = "-"

        max_ = 1e13
        min_ = 0
        while True:
            monkeys = deepcopy(self.monkeys)
            monkeys["humn"] = min_
            min_res = solve(monkeys)

            monkeys = deepcopy(self.monkeys)
            monkeys["humn"] = max_
            max_res = solve(monkeys)

            mid = (min_ + max_) // 2
            monkeys = deepcopy(self.monkeys)
            monkeys["humn"] = mid
            mid_res = solve(monkeys)

            if min_res == 0:
                answer = min_
                break
            elif max_res == 0:
                answer = max_
                break
            elif mid_res == 0:
                answer = mid
                break
            else:
                if sign(mid_res) == sign(max_res):
                    max_ = mid
                else:
                    min_ = mid
        print(int(answer))
        return int(answer)

    def save_results(self):
        with open(Path(__file__).parent / "part1", "w") as opened_file:
            opened_file.write(str(self.solve_part_1()))

        with open(Path(__file__).parent / "part2", "w") as opened_file:
            opened_file.write(str(self.solve_part_2()))


if __name__ == "__main__":
    solution = Solution()
    solution.save_results()
