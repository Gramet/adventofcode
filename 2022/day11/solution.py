from pathlib import Path

from tqdm import tqdm


class Monkey:
    def __init__(self, item_list, operation, test, divide=True):
        self.item_list = item_list
        self.op = self.inspect_op(operation)
        self.testval = test
        self.test = lambda x: (x % test) == 0
        self.true = None
        self.false = None
        self.count = 0
        self.mod = None
        self.divide = divide

    def inspect(self):
        while self.item_list:
            self.count += 1
            item = self.item_list.pop(0)
            if self.divide:
                new_item = self.op(item) // 3
            else:
                new_item = self.op(item) % self.mod
            test = self.test(new_item)
            if test:
                self.true.item_list.append(new_item)
            else:
                self.false.item_list.append(new_item)

    def inspect_op(self, operation):
        if operation[0] == "add":
            op = lambda x: x + operation[1]
        elif operation[0] == "mul":
            op = lambda x: x * operation[1]
        else:
            op = lambda x: x * x

        return op


class Solution:
    def __init__(self):
        with open(Path(__file__).parent / "input", "r") as f:
            self.input = f.readlines()

    def solve_part_1(self):
        m0 = Monkey([99, 63, 76, 93, 54, 73], ["mul", 11], 2)
        m1 = Monkey([91, 60, 97, 54], ["add", 1], 17)
        m2 = Monkey([65], ["add", 7], 7)
        m3 = Monkey([84, 55], ["add", 3], 11)
        m4 = Monkey([86, 63, 79, 54, 83], ["square"], 19)
        m5 = Monkey([96, 67, 56, 95, 64, 69, 96], ["add", 4], 5)
        m6 = Monkey([66, 94, 70, 93, 72, 67, 88, 51], ["mul", 5], 13)
        m7 = Monkey([59, 59, 74], ["add", 8], 3)

        m0.true = m7
        m0.false = m1
        m1.true = m3
        m1.false = m2
        m2.true = m6
        m2.false = m5
        m3.true = m2
        m3.false = m6
        m4.true = m7
        m4.false = m0
        m5.true = m4
        m5.false = m0
        m6.true = m4
        m6.false = m5
        m7.true = m1
        m7.false = m3
        for _ in range(20):
            m0.inspect()
            m1.inspect()
            m2.inspect()
            m3.inspect()
            m4.inspect()
            m5.inspect()
            m6.inspect()
            m7.inspect()
        counts = sorted([m.count for m in [m0, m1, m2, m3, m4, m5, m6, m7]])
        answer = counts[-1] * counts[-2]
        print(answer)
        return answer

    def solve_part_2(self):
        m0 = Monkey([99, 63, 76, 93, 54, 73], ["mul", 11], 2, False)
        m1 = Monkey([91, 60, 97, 54], ["add", 1], 17, False)
        m2 = Monkey([65], ["add", 7], 7, False)
        m3 = Monkey([84, 55], ["add", 3], 11, False)
        m4 = Monkey([86, 63, 79, 54, 83], ["square"], 19, False)
        m5 = Monkey([96, 67, 56, 95, 64, 69, 96], ["add", 4], 5, False)
        m6 = Monkey([66, 94, 70, 93, 72, 67, 88, 51], ["mul", 5], 13, False)
        m7 = Monkey([59, 59, 74], ["add", 8], 3, False)

        m0.true = m7
        m0.false = m1
        m1.true = m3
        m1.false = m2
        m2.true = m6
        m2.false = m5
        m3.true = m2
        m3.false = m6
        m4.true = m7
        m4.false = m0
        m5.true = m4
        m5.false = m0
        m6.true = m4
        m6.false = m5
        m7.true = m1
        m7.false = m3

        mod = 1
        for m in [m0, m1, m2, m3, m4, m5, m6, m7]:
            mod *= m.testval
        for m in [m0, m1, m2, m3, m4, m5, m6, m7]:
            m.mod = mod
        for _ in tqdm(range(10000)):
            m0.inspect()
            m1.inspect()
            m2.inspect()
            m3.inspect()
            m4.inspect()
            m5.inspect()
            m6.inspect()
            m7.inspect()
        counts = sorted([m.count for m in [m0, m1, m2, m3, m4, m5, m6, m7]])
        answer = counts[-1] * counts[-2]
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
