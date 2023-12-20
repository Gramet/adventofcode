from math import lcm
from pathlib import Path

from aoc_utils import *

INPUT_FILE = Path(__file__).parent / "input"


class Node:
    def __init__(self, type_, outputs):
        self.type_ = type_
        self.inputs = []
        self.outputs = outputs
        self.memory = {}
        self.value = 0

    def propagate(self, pulse, orig):
        if self.type_ == "%":
            if pulse == 1:
                pass
            else:
                self.value = 1 - self.value
                return self.value, self.outputs
        elif self.type_ == "&":
            self.memory[orig] = pulse
            if all(self.memory.values()):
                return 0, self.outputs
            else:
                return 1, self.outputs
        elif self.type_ == "b":
            return pulse, self.outputs

    def __eq__(self, other):
        return self.memory == other.memory and self.value == other.value

    def __str__(self):
        return f"{self.memory=}, {self.value=}"


class Solution:
    def __init__(self):
        self.input = read_input(INPUT_FILE)
        self.nodes = {}
        for line in self.input:
            name, outputs = line.strip().split(" -> ")
            outputs = outputs.split(", ")
            type_, name = name[0], name[1:]
            self.nodes[name] = Node(type_, outputs)
        output_nodes = {}
        for node_name, node in self.nodes.items():
            for out in node.outputs:
                if out not in self.nodes:
                    output_nodes[out] = Node(None, [])

        self.nodes.update((output_nodes))

        for node_name, node in self.nodes.items():
            for out in node.outputs:
                self.nodes[out].inputs.append(node_name)
                self.nodes[out].memory[node_name] = 0

    def solve_part_1(self):
        count = [0, 0]
        for i in range(1000):
            signals = [(0, "button", "roadcaster")]
            while signals:
                pulse, orig, dest = signals.pop(0)
                count[pulse] += 1
                result = self.nodes[dest].propagate(pulse, orig)
                if result is not None:
                    ret_pulse, outs = result
                    for out in outs:
                        signals.append((ret_pulse, dest, out))

        answer = count[0] * count[1]
        print(answer)
        return answer

    def solve_part_2(self):
        self.__init__()
        steps = 0
        nodes_to_check = {x: 0 for x in self.nodes["hf"].memory.keys()}
        while True:
            steps += 1
            signals = [(0, "button", "roadcaster")]
            while signals:
                pulse, orig, dest = signals.pop(0)
                if dest == "hf" and pulse == 1 and nodes_to_check[orig] == 0:
                    nodes_to_check[orig] = steps
                if dest == "rx" and pulse == 0:
                    answer = steps
                    print(answer)
                    return answer
                result = self.nodes[dest].propagate(pulse, orig)
                if result is not None:
                    ret_pulse, outs = result
                    for out in outs:
                        signals.append((ret_pulse, dest, out))
            if all(nodes_to_check.values()):
                break
        answer = lcm(*nodes_to_check.values())
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
