from pathlib import Path


def find_start(input_, buffer_len):
    for i in range(len(input_)):
        if len(set(input_[i : i + buffer_len])) == buffer_len:
            return i + buffer_len


class Solution:
    def __init__(self):
        with open(Path(__file__).parent / "input", "r") as f:
            self.input = f.readlines()[0]

    def solve_part_1(self):
        answer = find_start(self.input, 4)
        print(answer)
        return answer

    def solve_part_2(self):
        answer = find_start(self.input, 14)
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
