from pathlib import Path


class Solution:
    def __init__(self):
        with open(Path(__file__).parent / "input", "r") as f:
            self.input = f.readlines()

        self.allergens = {}
        self.all_ingrs = set()
        self.all_compos = []
        for line in self.input:
            compo, rest = line.split(" (contains ")
            allergs = rest.strip().strip(")").split(", ")
            ingrs = set(compo.split())
            self.all_compos.append(ingrs)
            self.all_ingrs = self.all_ingrs | ingrs
            for a in allergs:
                if a in self.allergens:
                    self.allergens[a] = self.allergens[a] & ingrs
                else:
                    self.allergens[a] = ingrs

    def solve_part_1(self):
        self.found = {}
        while len(self.found) < len(self.allergens):
            for a, ingrs in self.allergens.items():
                if len(ingrs) == 1:
                    self.found[a] = ingrs
                    for b, ingrs_b in self.allergens.items():
                        if b == a:
                            continue
                        self.allergens[b] = ingrs_b - ingrs

        safe_ingrs = self.all_ingrs.difference(list(x)[0] for x in self.found.values())

        answer = 0
        for compo in self.all_compos:
            for ingr in safe_ingrs:
                if ingr in compo:
                    answer += 1
        print(answer)
        return answer

    def solve_part_2(self):
        s = ""
        for k, v in sorted(self.found.items()):
            print(k, v)
            s += list(v)[0] + ","

        answer = s[:-1]
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
