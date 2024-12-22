from pathlib import Path

from aoc_utils import *

INPUT_FILE = Path(__file__).parent / "input"


def mix(secret, num):
    return secret ^ num


def prune(secret):
    return secret % 16777216


def iterate(secret):
    num = secret * 64
    secret = mix(secret, num)
    secret = prune(secret)

    num = secret // 32
    secret = mix(secret, num)
    secret = prune(secret)

    num = secret * 2048
    secret = mix(secret, num)
    secret = prune(secret)
    return secret


class Solution:
    def __init__(self):
        self.input = read_input(INPUT_FILE)

    def solve_part_1(self):
        answer = 0
        for line in self.input:
            secret = int(line)
            for _ in range(2000):
                secret = iterate(secret)
            answer += secret

        print(answer)
        return answer

    def solve_part_2(self):
        answer = 0
        all_seq_dict = defaultdict(int)
        for line in self.input:
            seq_dict = defaultdict(int)
            secret = int(line)
            cur_price = secret % 10
            last_four = (None, None, None, None)
            for i in range(2000):
                secret = iterate(secret)
                new_price = secret % 10
                last_four = last_four[1:] + (new_price - cur_price,)
                if i >= 3 and last_four not in seq_dict:
                    seq_dict[last_four] = new_price
                cur_price = new_price
            for k, v in seq_dict.items():
                all_seq_dict[k] += v

        answer = max(all_seq_dict.values())

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
