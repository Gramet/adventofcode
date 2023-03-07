from collections import Counter, defaultdict
from pathlib import Path


class Solution:
    def __init__(self):
        with open(Path(__file__).parent / "input", "r") as f:
            self.input = f.readlines()

        self.fish = list(map(int, self.input[0].strip("\n").split(",")))
        self.fish = Counter(self.fish)
        print(self.fish)

    def solve_part_1(self):
        for _ in range(80):
            new_fish = defaultdict(int)
            for k, v in self.fish.items():
                if k == 0:
                    new_fish[6] += v
                    new_fish[8] += v
                else:
                    new_fish[k - 1] += v

            self.fish = new_fish
        answer = sum(self.fish.values())
        print(answer)
        return answer

    def solve_part_2(self):
        self.fish = list(map(int, self.input[0].strip("\n").split(",")))
        self.fish = Counter(self.fish)
        for _ in range(256):
            new_fish = defaultdict(int)
            for k, v in self.fish.items():
                if k == 0:
                    new_fish[6] += v
                    new_fish[8] += v
                else:
                    new_fish[k - 1] += v

            self.fish = new_fish
        answer = sum(self.fish.values())
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
