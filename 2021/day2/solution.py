from pathlib import Path


class Solution:
    def __init__(self):
        with open(Path(__file__).parent / "input", "r") as f:
            self.input = f.readlines()

        self.commands = [(*l.strip("\n").split(" "),) for l in self.input]

    def solve_part_1(self):
        pos = 0
        depth = 0
        for command in self.commands:
            match command[0]:
                case "forward":
                    pos += int(command[1])
                case "down":
                    depth += int(command[1])
                case "up":
                    depth -= int(command[1])
        answer = depth * pos
        print(answer)
        return answer

    def solve_part_2(self):
        pos = 0
        depth = 0
        aim = 0
        for command in self.commands:
            match command[0]:
                case "forward":
                    pos += int(command[1])
                    depth += aim * int(command[1])
                case "down":
                    aim += int(command[1])
                case "up":
                    aim -= int(command[1])
        answer = depth * pos
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
