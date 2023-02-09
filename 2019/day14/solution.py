import math
import time
from collections import defaultdict
from copy import deepcopy
from pathlib import Path


def find_key(list_, key):
    for el in list_:
        if el[0] == key:
            return el


class Solution:
    def __init__(self):
        with open(Path(__file__).parent / "input", "r") as f:
            self.input = f.readlines()

        self.reactions = {}
        self.react_sets = {}
        for line in self.input:
            line = line.strip("\n")
            reactants = line.split("=>")[0]
            product = line.split("=>")[1]
            prod_amount = int(product.split()[0])
            prod = product.split()[1]
            reacts = []
            for reactant in reactants.split(","):
                react = reactant.split()[1]
                react_amount = int(reactant.split()[0])
                reacts.append((react, react_amount))
            self.reactions[(prod, prod_amount)] = reacts
            self.react_sets[prod] = set([r[0] for r in reacts])

        while True:
            new_reacts = deepcopy(self.react_sets)
            for prod, required_mats in new_reacts.items():
                new_required_mats = deepcopy(required_mats)
                for mat in required_mats:
                    if mat != "ORE":
                        new_required_mats |= new_reacts[mat]
                new_reacts[prod] = new_required_mats
            if new_reacts == self.react_sets:
                break
            else:
                self.react_sets = new_reacts

    def find_react(self, react):
        for k, v in self.reactions.items():
            if k[0] == react:
                return k, v

    def solve_part_1(self):
        reactants = deepcopy(self.reactions[("FUEL", 1)])
        leftovers = defaultdict(int)
        while any(r[0] != "ORE" for r in reactants):
            for react in reactants:
                if react[0] != "ORE" and not (
                    any(
                        react[0] in self.react_sets[x[0]]
                        for x in reactants
                        if x[0] != "ORE"
                    )
                ):
                    react_out, materials = self.find_react(react[0])
                    if react[1] <= leftovers[react[0]]:
                        num_to_react = 0
                        leftovers[react[0]] -= react[1]
                    else:
                        react_needed = react[1] - leftovers[react[0]]
                        num_to_react = max(
                            1,
                            math.ceil(react_needed / react_out[1]),
                        )
                        leftovers[react[0]] += (
                            num_to_react * react_out[1] - react_needed
                        )
                    for mat in materials:
                        if any(r[0] == mat[0] for r in reactants):
                            r = find_key(reactants, mat[0])
                            reactants.remove(r)
                            reactants.append((mat[0], r[1] + mat[1] * num_to_react))
                        else:
                            reactants.append((mat[0], mat[1] * num_to_react))
                    reactants.remove(react)
                    break
        answer = sum(r[1] for r in reactants)
        print(answer)
        return answer

    def solve_part_2(self):
        ORE = 1000000000000
        num_fuel = 2370000
        reactants = deepcopy(self.reactions[("FUEL", 1)])
        while True:
            self.reactions[("FUEL", 1)] = [(x[0], x[1] * num_fuel) for x in reactants]
            num_needed = self.solve_part_1()
            if num_needed > ORE:
                break
            num_fuel += 1
        answer = num_fuel - 1
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
