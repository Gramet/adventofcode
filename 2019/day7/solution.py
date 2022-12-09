from pathlib import Path
from copy import deepcopy
import itertools

POSITION_MODE = 0
VALUE_MODE = 1
import logging


class IntCodeComputer:
    def __init__(self, program, inputs=[]):
        self.program = program
        self.idx = 0
        self.answer = None
        self.inputs = inputs
        self.inputs_ptr = 0
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
        }

    def get_value(self, val, mode):
        mode = int(mode)
        if mode == POSITION_MODE:
            return int(self.program[int(val)])
        elif mode == VALUE_MODE:
            return int(val)
        else:
            raise NotImplementedError(f"mode={mode}")

    def adjust_param(self, params, param_length):
        return params.ljust(param_length, "0")

    def add(self, params):
        param_length = 3
        params = self.adjust_param(params, param_length)
        a = self.get_value(self.program[self.idx + 1], params[0])
        b = self.get_value(self.program[self.idx + 2], params[1])
        pos = self.get_value(self.program[self.idx + 3], VALUE_MODE)
        self.program[pos] = str(a + b)
        self.idx += param_length + 1
        logging.debug("add %i %i -> %i", a, b, pos)

    def multiply(self, params):
        param_length = 3
        params = self.adjust_param(params, param_length)
        a = self.get_value(self.program[self.idx + 1], params[0])
        b = self.get_value(self.program[self.idx + 2], params[1])
        pos = self.get_value(self.program[self.idx + 3], VALUE_MODE)
        self.program[pos] = str(a * b)
        self.idx += param_length + 1
        logging.debug("mult %i %i -> %i", a, b, pos)

    def input_(self, params):
        param_length = 1
        params = self.adjust_param(params, param_length)
        pos = self.get_value(self.program[self.idx + 1], VALUE_MODE)
        val = self.inputs[self.inputs_ptr]
        self.inputs_ptr += 1
        # val = input("Input required: ")
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
        pos = self.get_value(self.program[self.idx + 3], VALUE_MODE)
        self.program[pos] = int(val1 < val2)
        self.idx += param_length + 1
        logging.debug(f"lessthan %i %i -> %i", val1, val2, pos)

    def equals(self, params):
        param_length = 3
        params = self.adjust_param(params, param_length)
        val1 = self.get_value(self.program[self.idx + 1], params[0])
        val2 = self.get_value(self.program[self.idx + 2], params[1])
        pos = self.get_value(self.program[self.idx + 3], VALUE_MODE)
        self.program[pos] = int(val1 == val2)
        self.idx += param_length + 1
        logging.debug(f"equals %i %i -> %i", val1, val2, pos)

    def parse_opcode(self, val):
        opcode = int(str(val)[-2:])
        params = str(val)[:-2][::-1]
        return opcode, params

    def run(self):
        while True:
            op, params = self.parse_opcode(self.program[self.idx])
            logging.debug("%i %s", op, params)
            if op == 99:
                break
            else:
                self.op_dict[op](params)
                if op == 4:
                    break
        return self.answer, op


def amplifier_chain(program, phases):
    amp1, _ = IntCodeComputer(deepcopy(program), [phases[0], 0]).run()
    amp2, _ = IntCodeComputer(deepcopy(program), [phases[1], amp1]).run()
    amp3, _ = IntCodeComputer(deepcopy(program), [phases[2], amp2]).run()
    amp4, _ = IntCodeComputer(deepcopy(program), [phases[3], amp3]).run()
    amp5, _ = IntCodeComputer(deepcopy(program), [phases[4], amp4]).run()

    return amp5


def amplifier_chain_feedback(program, phases):
    amp1 = IntCodeComputer(deepcopy(program), [phases[0], 0])
    amp2 = IntCodeComputer(deepcopy(program), [phases[1]])
    amp3 = IntCodeComputer(deepcopy(program), [phases[2]])
    amp4 = IntCodeComputer(deepcopy(program), [phases[3]])
    amp5 = IntCodeComputer(deepcopy(program), [phases[4]])
    while True:
        out1, _ = amp1.run()
        amp2.inputs.append(out1)
        out2, _ = amp2.run()
        amp3.inputs.append(out2)
        out3, _ = amp3.run()
        amp4.inputs.append(out3)
        out4, _ = amp4.run()
        amp5.inputs.append(out4)
        out5, op = amp5.run()
        amp1.inputs.append(out5)
        if op == 99:
            return out5


class Solution:
    def __init__(self):
        with open(Path(__file__).parent / "input", "r") as f:
            self.input = f.readlines()[0].strip().split(",")
            self.input = [x for x in self.input]

    def solve_part_1(self):
        phases = itertools.permutations([0, 1, 2, 3, 4], 5)
        max_ = -1
        for phase in phases:
            max_ = max(max_, amplifier_chain(self.input, phase))
        answer = max_
        print(answer)
        return answer

    def solve_part_2(self):
        phases = itertools.permutations([5, 6, 7, 8, 9], 5)
        max_ = -1
        for phase in phases:
            max_ = max(max_, amplifier_chain_feedback(self.input, phase))
        answer = max_
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
