from pathlib import Path


def compute(lines):
    list_passed = []
    acc = 0
    ind = 0
    while (ind not in list_passed) and (ind < len(lines)):
        list_passed.append(ind)
        line = lines[ind]
        instr = line.split(" ")[0]
        val = int(line.split(" ")[1])
        if instr == "nop":
            ind += 1
        elif instr == "acc":
            acc += val
            ind += 1
        elif instr == "jmp":
            ind += val
    if ind >= len(lines):
        return acc, True, list_passed
    return acc, False, list_passed


class Solution:
    def __init__(self):
        with open(Path(__file__).parent / "input", "r") as f:
            self.input = f.readlines()

    def solve_part_1(self):
        acc, ret, list_passed = compute(self.input)
        answer = acc
        print(answer)
        return answer

    def solve_part_2(self):
        for ind, line in enumerate(self.input):
            val = int(line.split(" ")[1])
            instr = line.split(" ")[0]
            if instr == "nop":
                self.input[ind] = "{} {}".format("jmp", val)
                acc, ret, list_passed = compute(self.input)
                if ret:
                    break
                self.input[ind] = "{} {}".format("nop", val)
            if instr == "jmp":
                self.input[ind] = "{} {}".format("nop", val)
                acc, ret, list_passed = compute(self.input)
                if ret:
                    break
                self.input[ind] = "{} {}".format("jmp", val)
        answer = acc
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
