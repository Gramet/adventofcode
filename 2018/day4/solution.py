from pathlib import Path

from aoc_utils import *

INPUT_FILE = Path(__file__).parent / "input"


class Solution:
    def __init__(self):
        self.input = sorted(read_input(INPUT_FILE))

        self.guard_sleeps = {}
        for line in self.input:
            timestamp, log = line.split("] ")
            if log.startswith("Guard"):
                current_guard = parse_ints(log)[0]
                if current_guard not in self.guard_sleeps:
                    self.guard_sleeps[current_guard] = {m: 0 for m in range(60)}
            elif log.startswith("falls"):
                sleep_start = int(timestamp[-2:])

            else:
                sleep_end = int(timestamp[-2:])
                for minute in range(sleep_start, sleep_end):
                    self.guard_sleeps[current_guard][minute] += 1

    def solve_part_1(self):
        most_sleepy_guard = max(
            self.guard_sleeps, key=lambda x: sum(self.guard_sleeps[x].values())
        )
        most_sleepy_minute = max(
            self.guard_sleeps[most_sleepy_guard],
            key=self.guard_sleeps[most_sleepy_guard].get,
        )
        answer = most_sleepy_guard * most_sleepy_minute
        print(answer)
        return answer

    def solve_part_2(self):
        most_sleepy_guard = max(
            self.guard_sleeps, key=lambda x: max(self.guard_sleeps[x].values())
        )
        most_sleepy_minute = max(
            self.guard_sleeps[most_sleepy_guard],
            key=self.guard_sleeps[most_sleepy_guard].get,
        )
        answer = most_sleepy_guard * most_sleepy_minute
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
