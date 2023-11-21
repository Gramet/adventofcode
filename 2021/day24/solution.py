from functools import lru_cache
from pathlib import Path

from aoc_utils import read_input_parts

INPUT_FILE = Path(__file__).parent / "input"

memory_map = {"x": 0, "y": 1, "z": 2, "w": 3}


@lru_cache
def run_program(program, memory):
    memory_d = {"x": memory[0], "y": memory[1], "z": memory[2], "w": memory[3]}
    for line in program.split("\n"):
        command = line.strip().split(" ")
        match command[0]:
            case "mul":
                if command[2] in memory_d:
                    memory_d[command[1]] *= memory_d[command[2]]
                else:
                    memory_d[command[1]] *= int(command[2])
            case "add":
                if command[2] in memory_d:
                    memory_d[command[1]] += memory_d[command[2]]
                else:
                    memory_d[command[1]] += int(command[2])
            case "mod":
                if command[2] in memory_d:
                    memory_d[command[1]] %= memory_d[command[2]]
                else:
                    memory_d[command[1]] %= int(command[2])
            case "div":
                if command[2] in memory_d:
                    memory_d[command[1]] = memory_d[command[1]] // memory_d[command[2]]
                else:
                    memory_d[command[1]] = memory_d[command[1]] // int(command[2])
            case "eql":
                if command[2] in memory_d:
                    memory_d[command[1]] = memory_d[command[1]] == memory_d[command[2]]
                else:
                    memory_d[command[1]] = memory_d[command[1]] == int(command[2])

    return (memory_d["x"], memory_d["y"], memory_d["z"], memory_d["w"])


class Solution:
    def __init__(self):
        self.input = read_input_parts(INPUT_FILE)
        self.programs = self.input[0].split("inp w\n")[1:]

    def solve_part_1(self):
        # x and y value at the start of the program doesn't matter as they are reset to 0
        # They can be ignored from the states
        memory = 0
        inps = list(range(1, 10))
        states = {memory: 0}
        for program in self.programs:
            next_states = {}
            for state, best_inp in states.items():
                for inp in inps:
                    temp_memory = (0, 0, state, inp)
                    res = run_program(program, temp_memory)
                    if res[2] < 10000000:
                        # If z grows too big, it's not gonna come down ever
                        next_states[res[2]] = max(
                            next_states.get(res[2], 0),
                            best_inp * 10 + inp,
                        )
            states = next_states
            print(len(states))
        answer = states[0]
        print(answer)
        return answer

    def solve_part_2(self):
        # x and y value at the start of the program doesn't matter as they are reset to 0
        # They can be ignored from the states
        memory = 0
        inps = list(range(1, 10))
        states = {memory: 0}
        for program in self.programs:
            next_states = {}
            for state, best_inp in states.items():
                for inp in inps:
                    temp_memory = (0, 0, state, inp)
                    res = run_program(program, temp_memory)
                    if res[2] < 10000000:
                        # If z grows too big, it's not gonna come down ever
                        next_states[res[2]] = min(
                            next_states.get(res[2], 1e15),
                            best_inp * 10 + inp,
                        )
            states = next_states
            print(len(states))
        answer = states[0]
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
