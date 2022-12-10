from pathlib import Path


def addx(add_val, list_x, crt, crt_pos):
    crt, crt_pos = update_crt(list_x[-1], crt_pos, crt)
    list_x.append(list_x[-1])
    crt, crt_pos = update_crt(list_x[-1], crt_pos, crt)
    list_x.append(list_x[-1] + add_val)
    return list_x, crt, crt_pos


def update_crt(signal, crt_pos, crt):
    if abs(signal - (crt_pos % 40)) <= 1:
        crt += '#'
    else:
        crt += '.'
    crt_pos += 1
    return crt, crt_pos


def read_cpu_signal(signal):
    crt_pos = 0
    list_x = [1]
    crt = ''
    for line in signal:
        match line.strip().split(' ')[0]:
            case "noop":
                crt, crt_pos = update_crt(list_x[-1], crt_pos, crt)
                list_x.append(list_x[-1])
            case "addx":
                add_val = int(line.strip().split(' ')[1])
                list_x, crt, crt_pos = addx(add_val, list_x, crt, crt_pos)

    return list_x, crt


class Solution:
    def __init__(self):
        with open(Path(__file__).parent / "input", "r") as f:
            self.input = f.readlines()

    def solve_part_1(self):
        signals, _ = read_cpu_signal(self.input)
        answer = 0
        for i in range(20, 221, 40):
            answer += signals[i-1]*i
        print(answer)
        return answer

    def solve_part_2(self):
        _, crt = read_cpu_signal(self.input)
        print(crt[1:40])
        print(crt[41:80])
        print(crt[81:120])
        print(crt[121:160])
        print(crt[161:200])
        print(crt[201:])
        answer = "ZFBFHGUP"
        return answer

    def save_results(self):
        with open(Path(__file__).parent / "part1", "w") as opened_file:
            opened_file.write(str(self.solve_part_1()))

        with open(Path(__file__).parent / "part2", "w") as opened_file:
            opened_file.write(str(self.solve_part_2()))


if __name__ == "__main__":
    solution = Solution()
    solution.save_results()
