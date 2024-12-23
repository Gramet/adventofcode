from collections import defaultdict
from pathlib import Path

from aoc_utils import *

INPUT_FILE = Path(__file__).parent / "input"


class Solution:
    def __init__(self):
        self.input = read_input(INPUT_FILE)

    def solve_part_1(self):
        self.net = defaultdict(set)
        for line in self.input:
            c1, c2 = line.strip("\n").split("-")
            self.net[c1].add(c2)
            self.net[c2].add(c1)

        self.triplets = set()

        for comp, conn in self.net.items():
            for comp2 in conn:
                conn2 = self.net[comp2]
                for comp3 in conn2:
                    if comp3 in conn:
                        self.triplets.add(tuple(sorted([comp, comp2, comp3])))

        answer = 0
        for triplet in self.triplets:
            if any(x[0] == "t" for x in triplet):
                answer += 1
        print(answer)
        return answer

    def solve_part_2(self):
        max_clique = ("cw",)
        for t in self.triplets:
            tot_clique = set(t)
            while True:
                new_clique = tot_clique.copy()
                for comp, conn in self.net.items():
                    if all(x in conn for x in tot_clique):
                        new_clique.add(comp)
                        break
                if new_clique == tot_clique:
                    break
                tot_clique |= new_clique

            if len(tot_clique) > len(max_clique):
                max_clique = tot_clique
        answer = ",".join(sorted(max_clique))
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
