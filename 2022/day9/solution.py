from pathlib import Path


def update_t(H, T):
    diff = (H[0] - T[0], H[1] - T[1])
    if max(abs(x) for x in diff) <= 1:
        return T

    match diff:
        case (0, 2):
            return (T[0], T[1] + 1)
        case (0, -2):
            return (T[0], T[1] - 1)
        case (2, 0):
            return (T[0] + 1, T[1])
        case (-2, 0):
            return (T[0] - 1, T[1])

        case (1, 2):
            return (T[0] + 1, T[1] + 1)
        case (1, -2):
            return (T[0] + 1, T[1] - 1)
        case (2, 1):
            return (T[0] + 1, T[1] + 1)
        case (-2, 1):
            return (T[0] - 1, T[1] + 1)

        case (-1, 2):
            return (T[0] - 1, T[1] + 1)
        case (-1, -2):
            return (T[0] - 1, T[1] - 1)
        case (2, -1):
            return (T[0] + 1, T[1] - 1)
        case (-2, -1):
            return (T[0] - 1, T[1] - 1)

        case (2, 2):
            return (T[0] + 1, T[1] + 1)
        case (2, -2):
            return (T[0] + 1, T[1] - 1)
        case (-2, 2):
            return (T[0] - 1, T[1] + 1)
        case (-2, -2):
            return (T[0] - 1, T[1] - 1)

        case _:
            raise ValueError(f"{diff} not supported")


def update(H, T, cmd, visited):
    if visited is None:
        visited = set()
    dir, steps = cmd.split(" ")
    steps = int(steps)
    match dir:
        case "R":
            for _ in range(steps):
                H = (H[0] + 1, H[1])
                T[0] = update_t(H, T[0])
                for i in range(len(T) - 1):
                    T[i + 1] = update_t(T[i], T[i + 1])
                visited.add(T[-1])
        case "L":
            for _ in range(steps):
                H = (H[0] - 1, H[1])
                T[0] = update_t(H, T[0])
                for i in range(len(T) - 1):
                    T[i + 1] = update_t(T[i], T[i + 1])
                visited.add(T[-1])
        case "U":
            for _ in range(steps):
                H = (H[0], H[1] + 1)
                T[0] = update_t(H, T[0])
                for i in range(len(T) - 1):
                    T[i + 1] = update_t(T[i], T[i + 1])
                visited.add(T[-1])
        case "D":
            for _ in range(steps):
                H = (H[0], H[1] - 1)
                T[0] = update_t(H, T[0])
                for i in range(len(T) - 1):
                    T[i + 1] = update_t(T[i], T[i + 1])
                visited.add(T[-1])
    return H, T, visited


class Solution:
    def __init__(self):
        with open(Path(__file__).parent / "input", "r") as f:
            self.input = f.readlines()

    def solve_part_1(self):
        H = (0, 0)
        T = [(0, 0)]
        visited = None
        for line in self.input:
            H, T, visited = update(H, T, line, visited)
        answer = len(visited)
        print(answer)
        return answer

    def solve_part_2(self):
        H = (0, 0)
        T = [(0, 0) for i in range(9)]
        visited = None
        for line in self.input:
            H, T, visited = update(H, T, line, visited)
        answer = len(visited)
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
