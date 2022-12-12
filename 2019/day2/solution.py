from copy import deepcopy
from pathlib import Path


def add(program, i):
    a = program[program[i + 1]]
    b = program[program[i + 2]]
    pos = program[i + 3]
    program[pos] = a + b
    return program, i + 4


def multiply(program, i):
    a = program[program[i + 1]]
    b = program[program[i + 2]]
    pos = program[i + 3]
    program[pos] = a * b
    return program, i + 4


op_dict = {1: add, 2: multiply}


def intcode(program):
    i = 0
    while True:
        op = program[i]
        if op == 99:
            break
        else:
            program, i = op_dict[op](program, i)
    return program


class Solution:
    def __init__(self):
        with open(Path(__file__).parent / "input", "r") as f:
            self.input = f.readlines()[0].split(",")
            self.input = [int(x) for x in self.input]

    def solve_part_1(self):
        program = deepcopy(self.input)
        program[1] = 12
        program[2] = 2
        answer = intcode(program)[0]
        print(answer)
        return answer

    def solve_part_2(self):
        for noun in range(0, 100):
            for verb in range(0, 100):
                program = deepcopy(self.input)
                program[1] = noun
                program[2] = verb
                if intcode(program)[0] == 19690720:
                    answer = 100 * noun + verb
                    print(answer)
                    return answer

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
