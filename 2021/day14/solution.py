from pathlib import Path
from collections import Counter
from copy import deepcopy
from math import ceil


class Solution:
    def __init__(self):
        with open(Path(__file__).parent / "input", "r") as f:
            self.input = f.readlines()

        self.polymer = self.input[0].strip("\n")

        self.rules = {}
        for rule in self.input[2:]:
            k, v = rule.strip("\n").split(" -> ")
            self.rules[k] = v

    def solve_part_1(self):
        for _ in range(10):
            new_polymer = ""
            for i in range(len(self.polymer) - 1):
                new_polymer += self.polymer[i]
                new_polymer += self.rules.get(self.polymer[i : i + 2], "")
            new_polymer += self.polymer[len(self.polymer) - 1 :]
            self.polymer = new_polymer

        count = Counter(self.polymer)
        answer = max(count.values()) - min(count.values())
        print(answer)
        return answer

    def solve_part_2(self):
        self.polymer = self.input[0].strip("\n")

        polymer_count = {}
        for i in range(len(self.polymer) - 1):
            pair = self.polymer[i : i + 2]
            polymer_count[pair] = polymer_count.get(pair, 0) + 1
        for _ in range(40):
            new_polymer_count = {}
            for pair, count in polymer_count.items():
                output = self.rules[pair]
                new_polymer_count[pair[0] + output] = count + new_polymer_count.get(
                    pair[0] + output, 0
                )
                new_polymer_count[output + pair[1]] = count + new_polymer_count.get(
                    output + pair[1], 0
                )

            polymer_count = new_polymer_count

        letter_count = {}
        for pair, count in polymer_count.items():
            letter_count[pair[0]] = count + letter_count.get(pair[0], 0)
            letter_count[pair[1]] = count + letter_count.get(pair[1], 0)
        letter_count[self.polymer[0]] += 1
        letter_count[self.polymer[-1]] += 1
        letter_count = {k: v / 2 for k, v in letter_count.items()}
        answer = int(max(letter_count.values()) - min(letter_count.values()))
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
