from pathlib import Path


def generate_adds(add):
    l = [add]
    while any("X" in a for a in l):
        for a in l:
            if "X" in a:
                l.append(a.replace("X", "0", 1))
                l.append(a.replace("X", "1", 1))
                l.remove(a)

    return l


class Solution:
    def __init__(self):
        with open(Path(__file__).parent / "input", "r") as f:
            self.input = f.readlines()

    def solve_part_1(self):
        mem = {}
        mask = ""
        for line in self.input:
            if line.startswith("mask"):
                mask = line.strip().split(" = ")[1]
            elif line.startswith("mem"):
                add = int(line.split("[")[1].split("]")[0])
                val = "{0:b}".format(int(line.strip().split(" = ")[1]))
                val = "0" * (36 - len(val)) + val
                mem[add] = "".join(
                    [v if x == "X" else x for x, v in zip(mask, val)])

        answer = sum(int(v, 2) for v in mem.values())
        print(answer)
        return answer

    def solve_part_2(self):
        mem = {}
        mask = ""
        for line in self.input:
            if line.startswith("mask"):
                mask = line.strip().split(" = ")[1]
            elif line.startswith("mem"):
                add = "{0:b}".format(int(line.split("[")[1].split("]")[0]))
                add = "0" * (36 - len(add)) + add
                add = "".join([x if (x == "X" or x == "1")
                               else v for x, v in zip(mask, add)])
                val = "{0:b}".format(int(line.strip().split(" = ")[1]))
                val = "0" * (36 - len(val)) + val
                adds = generate_adds(add)
                for a in adds:
                    mem[a] = val
        answer = sum(int(v, 2) for v in mem.values())
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
