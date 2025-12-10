from pathlib import Path

import numpy as np
from scipy.optimize import linprog

from aoc_utils import *

INPUT_FILE = Path(__file__).parent / "input"


class Solution:
    def __init__(self):
        self.input = read_input(INPUT_FILE)

    def solve_part_1(self):
        answer = 0
        for line in self.input:
            target_pattern = line.split("] ")[0][1:]
            target_pattern = set([i for i, c in enumerate(target_pattern) if c == "#"])
            # print(target_pattern)
            buttons = line.split("] ")[1].split(" {")[0].split(" ")
            buttons = [set(parse_ints(b)) for b in buttons]

            # print(buttons)

            num_presses = 1
            available_patterns = buttons
            seen_patterns = set()
            matched = False
            while not matched:
                for p in available_patterns:
                    if p == target_pattern:
                        answer += num_presses
                        # print(f"Matched in {num_presses} presses")
                        matched = True
                        break
                    seen_patterns.add(frozenset(p))
                new_patterns = (
                    set(
                        [
                            frozenset(p1 ^ p2)
                            for p1 in available_patterns
                            for p2 in buttons
                        ]
                    )
                    - seen_patterns
                )
                if not new_patterns:
                    # print("No more patterns")
                    break
                available_patterns = new_patterns
                num_presses += 1
        print(answer)
        return answer

    def solve_part_2(self):
        answer = 0
        for line in self.input:
            buttons = line.split("] ")[1].split(" {")[0].split(" ")
            buttons = sorted(
                [set(parse_ints(b)) for b in buttons], key=len, reverse=True
            )

            joltage = parse_ints(line.split("{")[1])
            button_np = []
            for b in buttons:
                button_array = np.array(np.zeros(len(joltage)))
                for idx in b:
                    button_array[idx] = 1
                button_np.append(button_array)
            button_np = np.array(button_np).T
            joltage = np.array(joltage)

            A = button_np
            b = joltage
            m, n = A.shape

            c = np.hstack([np.ones(n), np.zeros(n)])
            A_eq = np.hstack([A, np.zeros((m, n))])
            b_eq = b

            res = linprog(c, A_eq=A_eq, b_eq=b_eq, integrality=1)
            answer += int(res.fun)
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
