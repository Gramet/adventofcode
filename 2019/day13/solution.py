from collections import defaultdict
from copy import deepcopy
from pathlib import Path
from time import sleep

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
        self.screen = defaultdict(int)
        self.score = 0
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
        val = self.display_screen()
        # val = self.inputs[self.inputs_ptr]
        # self.inputs_ptr += 1
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

    def display_screen(self):
        if len(self.screen) != 0:
            max_x = max(x[0] for x in self.screen.keys())
            max_y = max(x[1] for x in self.screen.keys())
            paddle = 0
            ball = 0
            screen_str = ""
            for line in range(max_y + 1):
                for col in range(max_x + 1):
                    pix = self.screen[(col, line)]
                    match pix:
                        case 0:
                            screen_str += " "
                        case 1:
                            screen_str += "#"
                        case 2:
                            screen_str += "█"
                        case 3:
                            screen_str += "_"
                            paddle = col
                        case 4:
                            screen_str += "O"
                            ball = col
                screen_str += "\n"
            screen_str += f"\nscore: {self.score}"
            print("\33[2J")  # Clear terminal
            print(screen_str, end="\r")
            sleep(0.001)
            if paddle == ball:
                return 0
            elif paddle <= ball:
                return 1
            else:
                return -1


dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]


class Solution:
    def __init__(self):
        with open(Path(__file__).parent / "input", "r") as f:
            self.input = f.readlines()[0].strip().split(",")
            self.input = [x for x in self.input]
            self.input = defaultdict(int, [(i, v) for i, v in enumerate(self.input)])

    def solve_part_1(self):
        comp = IntCodeComputer(deepcopy(self.input))
        rets = []
        opcode = -1
        screen = defaultdict(int)
        while opcode != 99:
            ret, opcode = comp.run()
            rets.append(ret)
        for i in range(0, len(rets) - 1, 3):
            x = rets[i]
            y = rets[i + 1]
            screen[(x, y)] = int(rets[i + 2])

        answer = 0
        for obj in screen.values():
            if obj == 2:
                answer += 1

        print(answer)
        return answer

    def solve_part_2(self):
        free_play = deepcopy(self.input)
        free_play[0] = 2
        comp = IntCodeComputer(free_play)
        rets = []
        opcode = -1
        while opcode != 99:
            ret, opcode = comp.run()
            rets.append(ret)
            if len(rets) == 3:
                x = rets[0]
                y = rets[1]
                if x == -1 and y == 0:
                    comp.score = int(rets[2])
                    # print(f"score: {score}")
                else:
                    comp.screen[(x, y)] = int(rets[2])
                rets = []
        answer = comp.score
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
