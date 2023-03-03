from collections import Counter
from pathlib import Path
from statistics import mode


class Solution:
    def __init__(self):
        with open(Path(__file__).parent / "input", "r") as f:
            self.input = f.readlines()
            self.num_bits = len(self.input[0].strip("\n"))

    def solve_part_1(self):
        gamma = ""
        epsilon = ""
        for pos in range(self.num_bits):
            bits = [line[pos] for line in self.input]
            most_frequent = mode(bits)
            gamma += most_frequent
            if most_frequent == "1":
                epsilon += "0"
            else:
                epsilon += "1"

        gamma = int(gamma, 2)
        epsilon = int(epsilon, 2)
        answer = gamma * epsilon
        print(answer)
        return answer

    def solve_part_2(self):
        oxy = ""
        co2 = ""
        for pos in range(self.num_bits):
            oxy_bits = [line[pos] for line in self.input if line.startswith(oxy)]
            if len(oxy_bits) == 1:
                oxy = [line for line in self.input if line.startswith(oxy)][0]
                break
            count_oxy = Counter(oxy_bits)
            if count_oxy["1"] >= count_oxy["0"]:
                oxy += "1"
            else:
                oxy += "0"

        for pos in range(self.num_bits):
            co_bits = [line[pos] for line in self.input if line.startswith(co2)]
            if len(co_bits) == 1:
                co2 = [line for line in self.input if line.startswith(co2)][0]
                break
            count_co = Counter(co_bits)
            if count_co["1"] >= count_co["0"]:
                co2 += "0"
            else:
                co2 += "1"

        answer = int(oxy, 2) * int(co2, 2)

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
