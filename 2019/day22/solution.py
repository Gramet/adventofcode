from pathlib import Path


class Solution:
    def __init__(self):
        with open(Path(__file__).parent / "input", "r") as f:
            self.input = f.readlines()

    def solve_part_1(self):
        stack_len = 10007
        stack = list(range(stack_len))
        for line in self.input:
            if "new" in line:
                stack = list(reversed(stack))
            if "cut" in line:
                cut_num = int(line.split(" ")[1])
                if cut_num < 0:
                    cut_num = len(stack) + cut_num
                stack = stack[cut_num:] + stack[:cut_num]
            if "increment" in line:
                increment = int(line.split(" ")[-1])

                indices = [x * increment % len(stack) for x in range(len(stack))]
                new_list = [-1] * len(stack)
                for ind, card in zip(indices, stack):
                    new_list[ind] = card
                stack = new_list
        answer = stack.index(2019)
        print(answer)
        return answer

    def solve_part_2(self):
        stack_len = 119315717514047
        # stack_len = 10
        num_shuffle = 101741582076661
        # Model each shuffle as an affine function mod n
        a = 1
        b = 0
        for line in self.input:
            if "new" in line:
                a *= -1
                b += a
            if "cut" in line:
                cut_num = int(line.split(" ")[1])
                b += (cut_num * a) % stack_len
            if "increment" in line:
                increment = int(line.split(" ")[-1])
                a *= pow(increment, -1, stack_len)
            a = a % stack_len
            b = b % stack_len

        print(f"{a} * x + {b}")
        # y_n = a^n * x + sum_0_n-1(a^k * b)
        a_n = pow(a, num_shuffle, stack_len)
        bsum_ak = b * (1 - a_n) * pow(1 - a, -1, stack_len)
        answer = a_n * 2020 + bsum_ak
        print(a_n)
        print(bsum_ak)
        answer = answer % stack_len
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
