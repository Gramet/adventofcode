from pathlib import Path
import collections


class Solution:
    def __init__(self):
        with open(Path(__file__).parent / "input", "r") as f:
            self.input = f.readlines()
            self.adapters = sorted([int(line) for line in self.input])
            self.adapters.insert(0, 0)
            self.adapters.append(max(self.adapters) + 3)

    def solve_part_1(self):
        s1 = 0
        s3 = 0
        for i in range(1, len(self.adapters)):
            diff = self.adapters[i] - self.adapters[i - 1]
            if diff == 1:
                s1 += 1
            elif diff == 3:
                s3 += 1
        answer = s1 * s3
        print(answer)
        return answer

    def solve_part_2(self):
        cache = collections.defaultdict(int, {0: 1})

        for jolt in self.adapters:
            for possible in (jolt - 1, jolt - 2, jolt - 3):
                if possible in cache:
                    cache[jolt] += cache[possible]

        answer = cache[self.adapters[-1]]
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
