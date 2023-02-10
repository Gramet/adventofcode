import itertools
from pathlib import Path

from tqdm import tqdm


class Solution:
    def __init__(self):
        with open(Path(__file__).parent / "input", "r") as f:
            self.input = list(map(int, list(f.readlines()[0].strip())))
        print(self.input)
        print(len(self.input))

    def fft(self, inp, pat):
        out = []
        for rep in range(len(inp)):
            pattern = list(
                itertools.islice(
                    itertools.cycle(
                        list(
                            itertools.chain.from_iterable(
                                itertools.repeat(x, rep + 1) for x in pat
                            )
                        )
                    ),
                    1,
                    len(inp) + 1,
                )
            )
            out.append(abs(sum(x * y for x, y in zip(inp, pattern))) % 10)
        return out

    def fft2(self, inp):
        out = []
        s = sum(inp)
        for i in range(len(inp)):
            out.append(s % 10)
            s = abs(s - inp[i])
        return out

    def solve_part_1(self):
        base_pattern = [0, 1, 0, -1]
        inp = self.input
        for _ in range(100):
            inp = self.fft(inp, base_pattern)
        answer = "".join(list(map(str, inp[:8])))
        print(answer)
        return answer

    def solve_part_2(self):
        offset = int("".join(list(map(str, self.input[:7]))))
        # Offset is huge, so we will only look at the latter part of the signal
        # The repeated pattern in the latter part is always 0000...1111...
        # which means first nunmbers are not needed and each new digit is always the sum of the latter ones
        inp = self.input * 10000
        inp = inp[offset:]
        for _ in tqdm(range(100)):
            inp = self.fft2(inp)
        answer = "".join(list(map(str, inp[:8])))
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
