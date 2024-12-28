from pathlib import Path

from aoc_utils import *

INPUT_FILE = Path(__file__).parent / "input"


class Solution:
    def __init__(self):
        self.inputs, self.gates = read_input_parts(INPUT_FILE)
        self.input_dict = {}
        for line in self.inputs.splitlines():
            inp, val = line.split(": ")
            self.input_dict[inp] = int(val)

        self.gates_dict = {}
        for gate in self.gates.splitlines():
            inp1, op, inp2, _, out = gate.split(" ")
            self.gates_dict[out] = (inp1, op, inp2)

    def eval_input(self, inp):
        if inp.startswith("x") or inp.startswith("y"):
            inp = self.input_dict[inp]
        else:
            inp = self.compute(self.gates_dict[inp])
        return inp

    def compute(self, gate):
        inp1, op, inp2 = gate
        inp1 = self.eval_input(inp1)
        inp2 = self.eval_input(inp2)
        if op == "AND":
            return inp1 & inp2
        elif op == "OR":
            return inp1 | inp2
        elif op == "XOR":
            return inp1 ^ inp2

    def solve_part_1(self):
        output_vals = {}
        for out, gate in self.gates_dict.items():
            if out.startswith("z"):
                output_vals[out] = self.compute(gate)

        out_str = "".join(str(output_vals[out]) for out in sorted(output_vals))[::-1]
        answer = int(out_str, 2)
        self.actual_z = out_str
        print(answer)
        return answer

    def solve_part_2(self):
        wrong = set()
        for gate_output, gate in self.gates_dict.items():
            inp1, op, inp2 = gate
            if gate_output[0] == "z" and op != "XOR" and gate_output != "z45":
                print(gate + (gate_output,))
                wrong.add(gate_output)
            elif (
                op == "XOR"
                and gate_output[0] not in ["x", "y", "z"]
                and inp1[0] not in ["x", "y", "z"]
                and inp2[0] not in ["x", "y", "z"]
            ):
                print(gate + (gate_output,))
                wrong.add(gate_output)
            elif op == "AND" and "x00" not in [inp1, inp2]:
                for subinp1, subop, subinp2 in self.gates_dict.values():
                    if (
                        gate_output == subinp1 or gate_output == subinp2
                    ) and subop != "OR":
                        print(gate + (gate_output,))
                        wrong.add(gate_output)
                        break
            elif op == "XOR":
                for subinp1, subop, subinp2 in self.gates_dict.values():
                    if (
                        gate_output == subinp1 or gate_output == subinp2
                    ) and subop == "OR":
                        print(gate + (gate_output,))
                        wrong.add(gate_output)
                        break

        answer = ",".join(sorted(wrong))

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
