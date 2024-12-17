from pathlib import Path

from aoc_utils import *

INPUT_FILE = Path(__file__).parent / "input"


class Solution:
    def __init__(self):
        self.registers, self.str_program = read_input_parts(INPUT_FILE)
        self.str_program = self.str_program.strip("\n")[9:]
        self.registers = parse_ints(self.registers)
        self.program = parse_ints(self.str_program)
        self.outputs = []

    def run(self, instr, literal_operand, combo_operand):
        match instr:
            case 0:
                self.registers[0] = self.registers[0] // (2**combo_operand)
            case 1:
                self.registers[1] = self.registers[1] ^ literal_operand
            case 2:
                self.registers[1] = combo_operand % 8
            case 3:
                if self.registers[0] != 0:
                    return literal_operand
            case 4:
                self.registers[1] = self.registers[1] ^ self.registers[2]
            case 5:
                self.outputs.append(str(combo_operand % 8))
            case 6:
                self.registers[1] = self.registers[0] // (2**combo_operand)
            case 7:
                self.registers[2] = self.registers[0] // (2**combo_operand)
        return None

    def parse_operand(self, operand):
        match operand:
            case 0 | 1 | 2 | 3:
                return operand
            case 4:
                return self.registers[0]
            case 5:
                return self.registers[1]
            case 6:
                return self.registers[2]
            case 7:
                return operand

    def solve_part_1(self):
        ptr = 0
        while True:
            if ptr >= len(self.program):
                break
            instr = self.program[ptr]
            operand = self.program[ptr + 1]
            combo_operand = self.parse_operand(operand)
            jmp = self.run(instr, operand, combo_operand)
            if jmp is not None:
                ptr = jmp
            else:
                ptr += 2

        answer = ",".join(self.outputs)
        print(answer)
        return answer

    def reverse_program(self):
        cur_a = {0}  # Program had to finish, so last a value was 0
        for value in self.program[::-1]:
            potential_a = []
            for previous_a in cur_a:
                for remainder in range(0, 8):
                    # This only work for my input program
                    a = previous_a * 8 + remainder
                    b = a % 8
                    b = b ^ 5
                    c = a // 2**b
                    b = b ^ c
                    b = b ^ 6
                    if b % 8 == value:
                        potential_a.append(a)
            cur_a = potential_a
        return cur_a

    def solve_part_2(self):
        potential_a = self.reverse_program()
        answer = min(potential_a)
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
