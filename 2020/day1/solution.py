from pathlib import Path


def two_sum(l, target):
    s = set(l)
    for num in l:
        diff = target - num
        if diff in s:
            return diff * num
    return None


def three_sum(l, target):
    s = set(l)
    for idx, num in enumerate(l):
        diff = target - num
        two_sum_res = two_sum(l[:idx] + l[idx + 1 :], diff)
        if two_sum_res is not None:
            return num * two_sum_res
    return None


class Solution:
    def __init__(self):
        with open(Path(__file__).parent / "input", "r") as f:
            self.input = f.readlines()
            self.input = [int(x) for x in self.input]

    def solve_part_1(self):
        answer = two_sum(self.input, 2020)
        print(answer)
        return answer

    def solve_part_2(self):
        answer = three_sum(self.input, 2020)
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
