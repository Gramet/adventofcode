from pathlib import Path
from copy import deepcopy


def full_orbits(x, orbits):
    if x == []:
        return 0
    tot = len(orbits[x])
    for orb in orbits[x]:
        tot += full_orbits(orb, orbits)
    return tot


def num_transfers(start, end, orbits):
    start_objs = set(orbits[start])
    end_objs = set(orbits[end])
    hist_start = [deepcopy(start_objs)]
    hist_end = [deepcopy(end_objs)]
    while True:
        if len(start_objs.intersection(end_objs)) != 0:
            x = start_objs.intersection(end_objs)
            num_transfer = [x.issubset(objs) for objs in hist_start].index(True) + [
                x.issubset(objs) for objs in hist_end
            ].index(True)
            return num_transfer
        else:
            new_objs = []
            for obj in start_objs:
                new_objs += orbits[obj]
            start_objs.update(new_objs)
            new_objs = []
            for obj in end_objs:
                new_objs += orbits[obj]
            end_objs.update(new_objs)
            hist_start.append(deepcopy(start_objs))
            hist_end.append(deepcopy(end_objs))


class Solution:
    def __init__(self):
        with open(Path(__file__).parent / "input", "r") as f:
            self.input = f.readlines()
        self.orbits = dict()
        for line in self.input:
            A, B = line.strip().split(")")
            self.orbits[A] = self.orbits.get(A, [])
            self.orbits[B] = self.orbits.get(B, [])
            self.orbits[B].append(A)

    def solve_part_1(self):
        answer = sum([full_orbits(x, self.orbits) for x in self.orbits.keys()])

        print(answer)
        return answer

    def solve_part_2(self):
        answer = num_transfers("YOU", "SAN", self.orbits)
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
