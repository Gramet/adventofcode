from pathlib import Path


def count_yes(group):
    s = set([])
    for person in group:
        s = s | set(person)
    return len(s)


def count_all_yes(group):
    s = set(group[0])
    for person in group:
        s = s & set(person)
    return len(s)


class Solution:
    def __init__(self):
        with open(Path(__file__).parent / "input", "r") as f:
            self.input = f.readlines()
        buff = []
        self.sum_yes = 0
        self.sum_all_yes = 0
        for line in self.input:
            if line == "\n":
                self.sum_all_yes += count_all_yes(buff)
                self.sum_yes += count_yes(buff)
                buff = []
            else:
                buff.append(line.strip("\n"))

        self.sum_yes += count_yes(buff)
        self.sum_all_yes += count_all_yes(buff)

    def solve_part_1(self):
        answer = self.sum_yes
        print(answer)
        return answer

    def solve_part_2(self):
        answer = self.sum_all_yes
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
