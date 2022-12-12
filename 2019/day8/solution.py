from collections import Counter
from pathlib import Path


def argmin(a):
    return min(range(len(a)), key=lambda x: a[x])


charmap = {"0": " ", "1": "▮"}


class Solution:
    def __init__(self):
        with open(Path(__file__).parent / "input", "r") as f:
            self.input = f.readlines()[0].strip()
        self.width = 25
        self.height = 6
        self.layer_size = self.width * self.height
        self.layers = [
            self.input[i : i + self.layer_size]
            for i in range(0, len(self.input), self.layer_size)
        ]

    def solve_part_1(self):
        counts = [Counter(layer) for layer in self.layers]
        best_layer = min(counts, key=lambda x: x["0"])
        answer = best_layer["1"] * best_layer["2"]
        print(answer)
        return answer

    def solve_part_2(self):
        out = self.layers[0]
        for layer in self.layers[1:]:
            for pos, val in enumerate(layer):
                if out[pos] == "2" and val != "2":
                    out = out[:pos] + val + out[pos + 1 :]

        char_out = "".join(charmap[i] for i in out)
        for i in range(0, len(char_out), self.width):
            print(char_out[i : i + self.width])
        answer = "GKCKH"
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
