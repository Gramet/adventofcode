import json
from copy import deepcopy
from math import ceil, floor
from pathlib import Path


def add_to_left_up(s, value):
    if s.parent is None:
        return
    if s.parent.left is s:
        add_to_left_up(s.parent, value)
    else:
        add_to_right_down(s.parent.left, value)


def add_to_right_up(s, value):
    if s.parent is None:
        return
    if s.parent.right is s:
        add_to_right_up(s.parent, value)
    else:
        add_to_left_down(s.parent.right, value)


def add_to_right_down(s, value):
    if s.value is not None:
        s.value += value
    else:
        add_to_right_down(s.right, value)


def add_to_left_down(s, value):
    if s.value is not None:
        s.value += value
    else:
        add_to_left_down(s.left, value)


class SnailFish:
    def __init__(self, left=None, right=None, value=None, parent=None):
        self.left = left
        self.right = right
        self.parent = parent
        self.value = value

    def __repr__(self) -> str:
        if self.value is not None:
            return str(self.value)
        else:
            return str((self.left, self.right))

    def explode(self, depth):
        if depth < 4:
            if self.left is not None:
                ret = self.left.explode(depth + 1)
                if ret:
                    return ret
            if self.right is not None:
                ret = self.right.explode(depth + 1)
                return ret
        else:
            if self.value is None:
                add_to_left_up(self, self.left.value)
                add_to_right_up(self, self.right.value)
                self.value = 0
                self.left = None
                self.right = None
                return True

    def split(self):
        if self.value is None:
            if self.left is not None:
                ret = self.left.split()
                if ret:
                    return ret
            if self.right is not None:
                ret = self.right.split()
                return ret
        else:
            if self.value >= 10:
                self.left = parse_number(floor(self.value / 2), parent=self)
                self.right = parse_number(ceil(self.value / 2), parent=self)
                self.value = None
                return True

    def reduce(self):
        while True:
            exploded = self.explode(depth=0)
            if exploded is None:
                splitted = self.split()
                if splitted is None:
                    return

    def magnitude(self):
        if self.value is not None:
            return self.value
        else:
            return 3 * self.left.magnitude() + 2 * self.right.magnitude()


def parse_number(number, parent) -> SnailFish:
    if isinstance(number, list):
        s = SnailFish()
        s.left = parse_number(number[0], parent=s)
        s.right = parse_number(number[1], parent=s)
        s.parent = parent
        return s
    else:
        s = SnailFish(value=number, parent=parent)
        return s


class Solution:
    def __init__(self):
        with open(Path(__file__).parent / "input", "r") as f:
            self.input = [json.loads(line.strip("\n")) for line in f.readlines()]

        self.numbers = [parse_number(x, parent=None) for x in self.input]

    def solve_part_1(self):
        numbers = deepcopy(self.numbers)
        current_num = numbers[0]
        for num in numbers[1:]:
            current_num = SnailFish(
                left=current_num, right=num, parent=None, value=None
            )
            current_num.left.parent = current_num
            current_num.right.parent = current_num
            current_num.reduce()
        answer = current_num.magnitude()
        print(answer)
        return answer

    def solve_part_2(self):
        answer = 0
        for i, num in enumerate(self.numbers):
            for num2 in self.numbers[i + 1 :]:
                num_ = deepcopy(num)
                num2_ = deepcopy(num2)
                current_num = SnailFish(left=num_, right=num2_)
                current_num.left.parent = current_num
                current_num.right.parent = current_num
                current_num.reduce()
                answer = max(answer, current_num.magnitude())
                num_ = deepcopy(num)
                num2_ = deepcopy(num2)
                current_num = SnailFish(left=num2_, right=num_)
                current_num.left.parent = current_num
                current_num.right.parent = current_num
                current_num.reduce()
                answer = max(answer, current_num.magnitude())
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
