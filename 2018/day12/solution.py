from pathlib import Path

from aoc_utils import *

INPUT_FILE = Path(__file__).parent / "input"


class Solution:
    def __init__(self):
        self.input = read_input_parts(INPUT_FILE)
        self.inital_state = self.input[0][15:]
        self.inital_state = {i: chr for i, chr in enumerate(self.inital_state)}
        self.rules = self.input[1].split("\n")

        self.rules_dict = {}
        for rule in self.rules[:-1]:
            self.rules_dict[rule[:5]] = rule[-1]

    def propagate(self, state):
        min_pot, max_pot = min(state.keys()), max(state.keys())
        new_state = {}
        for pos in range(min_pot - 2, max_pot + 3):
            neighbours = "".join(
                state.get(neigh, ".") for neigh in range(pos - 2, pos + 3)
            )
            new_state[pos] = self.rules_dict[neighbours]

        return new_state

    def solve_part_1(self):
        state = self.inital_state
        for _ in range(20):
            state = self.propagate(state)
        answer = sum(k for k, v in state.items() if v == "#")
        print(answer)
        return answer

    def solve_part_2(self):
        state = self.inital_state
        for e in range(2000):
            state = self.propagate(state)
            answer = sum(k for k, v in state.items() if v == "#")
            if e == 999:
                after_1000 = answer
                print(e, answer)
        delta = answer - after_1000
        answer = after_1000 + (50000000000 - 1000) // 1000 * delta
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
