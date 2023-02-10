from collections import defaultdict
from copy import deepcopy
from itertools import product
from pathlib import Path

POSITION_MODE = 0
VALUE_MODE = 1
RELATIVE_MODE = 2
import logging


class IntCodeComputer:
    def __init__(self, program, inputs=[]):
        self.program = program
        self.idx = 0
        self.answer = None
        self.inputs = inputs
        self.inputs_ptr = 0
        self.relative_base = 0
        logging.basicConfig(level=logging.ERROR)

        self.op_dict = {
            1: self.add,
            2: self.multiply,
            3: self.input_,
            4: self.output,
            5: self.jump_if_true,
            6: self.jump_if_false,
            7: self.less_than,
            8: self.equals,
            9: self.adjust_relative,
            99: self.pass_,
        }

    def get_address(self, val, mode):
        mode = int(mode)
        if mode == POSITION_MODE:
            return int(val)
        elif mode == RELATIVE_MODE:
            return int(val) + self.relative_base
        else:
            raise NotImplementedError(f"adress mode={mode}")

    def get_value(self, val, mode):
        mode = int(mode)
        if mode == POSITION_MODE:
            return int(self.program[int(val)])
        elif mode == VALUE_MODE:
            return int(val)
        elif mode == RELATIVE_MODE:
            return int(self.program[int(val) + self.relative_base])
        else:
            raise NotImplementedError(f"mode={mode}")

    def adjust_param(self, params, param_length):
        return params.ljust(param_length, "0")

    def adjust_relative(self, params):
        param_length = 1
        params = self.adjust_param(params, param_length)
        val = self.get_value(self.program[self.idx + 1], params[0])
        self.relative_base += val
        self.idx += param_length + 1
        logging.debug("adjust relative base by %i to %i", val, self.relative_base)

    def add(self, params):
        param_length = 3
        params = self.adjust_param(params, param_length)
        a = self.get_value(self.program[self.idx + 1], params[0])
        b = self.get_value(self.program[self.idx + 2], params[1])
        pos = self.get_address(self.program[self.idx + 3], params[2])
        self.program[pos] = str(a + b)
        self.idx += param_length + 1
        logging.debug("add %i %i -> %i", a, b, pos)

    def multiply(self, params):
        param_length = 3
        params = self.adjust_param(params, param_length)
        a = self.get_value(self.program[self.idx + 1], params[0])
        b = self.get_value(self.program[self.idx + 2], params[1])
        pos = self.get_address(self.program[self.idx + 3], params[2])
        self.program[pos] = str(a * b)
        self.idx += param_length + 1
        logging.debug("mult %i %i -> %i", a, b, pos)

    def input_(self, params):
        param_length = 1
        params = self.adjust_param(params, param_length)
        pos = self.get_address(self.program[self.idx + 1], params[0])
        val = self.inputs[self.inputs_ptr]
        self.inputs_ptr += 1
        self.program[pos] = val
        self.idx += param_length + 1
        logging.debug("input %i -> %i", val, pos)

    def output(self, params):
        param_length = 1
        params = self.adjust_param(params, param_length)
        val = self.get_value(self.program[self.idx + 1], params[0])
        self.answer = val
        logging.info("output: %i", val)
        self.idx += param_length + 1

    def jump_if_true(self, params):
        param_length = 2
        params = self.adjust_param(params, param_length)
        val = self.get_value(self.program[self.idx + 1], params[0])
        if val:
            self.idx = self.get_value(self.program[self.idx + 2], params[1])
            logging.debug("jumptrue %i", self.idx)
        else:
            self.idx += param_length + 1

    def jump_if_false(self, params):
        param_length = 2
        params = self.adjust_param(params, param_length)
        val = self.get_value(self.program[self.idx + 1], params[0])
        if not val:
            self.idx = self.get_value(self.program[self.idx + 2], params[1])
            logging.debug(f"jumpfalse %i", self.idx)
        else:
            self.idx += param_length + 1

    def less_than(self, params):
        param_length = 3
        params = self.adjust_param(params, param_length)
        val1 = self.get_value(self.program[self.idx + 1], params[0])
        val2 = self.get_value(self.program[self.idx + 2], params[1])
        pos = self.get_address(self.program[self.idx + 3], params[2])
        self.program[pos] = int(val1 < val2)
        self.idx += param_length + 1
        logging.debug(f"lessthan %i %i -> %i", val1, val2, pos)

    def equals(self, params):
        param_length = 3
        params = self.adjust_param(params, param_length)
        val1 = self.get_value(self.program[self.idx + 1], params[0])
        val2 = self.get_value(self.program[self.idx + 2], params[1])
        pos = self.get_address(self.program[self.idx + 3], params[2])
        self.program[pos] = int(val1 == val2)
        self.idx += param_length + 1
        logging.debug(f"equals %i %i -> %i", val1, val2, pos)

    def pass_(self, params):
        pass

    def parse_opcode(self, val):
        opcode = int(str(val)[-2:])
        params = str(val)[:-2][::-1]
        return opcode, params

    def run(self):
        while True:
            op, params = self.parse_opcode(self.program[self.idx])
            logging.debug("%i %s", op, params)
            self.op_dict[op](params)
            if op in [4, 99]:
                break
        return self.answer, op


dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]

dirs_delta = {1: (0, 1), 2: (0, -1), 3: (-1, 0), 4: (1, 0)}


def get_square(inputs):
    pos = (0, 0)
    for dir in inputs:
        pos = (pos[0] + dirs_delta[dir][0], pos[1] + dirs_delta[dir][1])
    return pos


class Solution:
    def __init__(self):
        with open(Path(__file__).parent / "input", "r") as f:
            self.input = f.readlines()[0].strip().split(",")
            self.input = [x for x in self.input]
            self.input = defaultdict(int, [(i, v) for i, v in enumerate(self.input)])
        self.map = defaultdict(int)
        self.map[(0, 0)] = 1

    def solve_part_1(self):
        self.paths_to_check = [[1], [2], [3], [4]]
        while self.paths_to_check:
            self.paths_to_check = sorted(self.paths_to_check, key=len, reverse=True)
            while self.paths_to_check:
                inp = self.paths_to_check.pop(0)
                if get_square(inp) not in self.map:
                    break
            comp = IntCodeComputer(deepcopy(self.input), inp)
            for _ in inp:
                ret, opcode = comp.run()
            if ret == 2:
                self.map[get_square(inp)] = 2
                answer = len(inp)
                print(answer)
                return answer
            elif ret == 1:
                square = get_square(inp)
                self.map[square] = 1
                for dir in [1, 2, 3, 4]:
                    if get_square(inp + [dir]) not in self.map:
                        self.paths_to_check.append(inp + [dir])
            elif ret == 0:
                square = get_square(inp)
                self.map[square] = 0

    def solve_part_2(self):
        # Finish checking all paths
        while self.paths_to_check:
            self.paths_to_check = sorted(self.paths_to_check, key=len, reverse=True)
            while self.paths_to_check:
                inp = self.paths_to_check.pop(0)
                if get_square(inp) not in self.map:
                    break
            comp = IntCodeComputer(deepcopy(self.input), inp)
            for _ in inp:
                ret, opcode = comp.run()
            if ret == 2:
                self.map[get_square(inp)] = 2
                answer = len(inp)
            elif ret == 1:
                square = get_square(inp)
                self.map[square] = 1
                for dir in [1, 2, 3, 4]:
                    if get_square(inp + [dir]) not in self.map:
                        self.paths_to_check.append(inp + [dir])
            elif ret == 0:
                square = get_square(inp)
                self.map[square] = 0

        # Fill oxygen from the source
        num_steps = 0
        while any(val == 1 for val in self.map.values()):
            num_steps += 1
            oxy_squares = [square for square, val in self.map.items() if val == 2]
            for square in oxy_squares:
                for delta in dirs_delta.values():
                    adj_square = (square[0] + delta[0], square[1] + delta[1])
                    if self.map[adj_square] == 1:
                        self.map[adj_square] = 2

        answer = num_steps
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
