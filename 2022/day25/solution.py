from pathlib import Path


def snafu_to_int(num):
    res = 0
    for i, char in enumerate(num[::-1]):
        match char:
            case "2":
                res += 2 * 5**i
            case "1":
                res += 5**i
            case "0":
                pass
            case "-":
                res -= 5**i
            case "=":
                res -= 2 * 5**i
    return res


def int_to_snafu(num):
    test = 0
    digit = 0
    while test < num:
        test += 2 * 5**digit
        digit += 1
    snafu = "2" * digit
    print(digit)
    for i, char in enumerate(snafu):
        if test == num:
            return snafu
        if test - 5 ** (digit - i - 1) < num:
            pass
        elif test - 2 * 5 ** (digit - i - 1) < num:
            snafu = snafu[:i] + "1" + snafu[i + 1 :]
            test = test - 1 * 5 ** (digit - i - 1)

        elif test - 3 * 5 ** (digit - i - 1) < num:
            snafu = snafu[:i] + "0" + snafu[i + 1 :]
            test = test - 2 * 5 ** (digit - i - 1)

        elif test - 4 * 5 ** (digit - i - 1) < num:
            snafu = snafu[:i] + "-" + snafu[i + 1 :]
            test = test - 3 * 5 ** (digit - i - 1)
        else:
            snafu = snafu[:i] + "=" + snafu[i + 1 :]
            test = test - 4 * 5 ** (digit - i - 1)
        print(snafu, test, num)

    return snafu


class Solution:
    def __init__(self):
        with open(Path(__file__).parent / "input", "r") as f:
            self.input = f.readlines()
            self.input = [l.strip() for l in self.input]

    def solve_part_1(self):
        tot = 0
        for snafu in self.input:
            tot += snafu_to_int(snafu)

        answer = int_to_snafu(tot)
        print(answer)
        return answer

    def solve_part_2(self):
        answer = "None"
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
