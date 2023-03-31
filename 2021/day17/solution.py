from pathlib import Path


class Solution:
    def __init__(self):
        with open(Path(__file__).parent / "input", "r") as f:
            self.input = f.readlines()[0].strip("\n")

        self.min_x, self.max_x = self.input.split(",")[0].split("=")[1].split("..")
        self.min_y, self.max_y = self.input.split(",")[1].split("=")[1].split("..")
        self.min_x = int(self.min_x)
        self.max_x = int(self.max_x)
        self.min_y = int(self.min_y)
        self.max_y = int(self.max_y)

        print(self.min_x, self.max_x, self.min_y, self.max_y)

    def compute_traj(self, x, y):
        traj = [(0, 0)]
        pos = (0, 0)
        hit_target = False
        while pos[0] <= self.max_x and pos[1] >= self.min_y:
            pos = (pos[0] + x, pos[1] + y)
            x = max(x - 1, 0)
            y -= 1
            traj.append(pos)
            if (
                self.min_x <= pos[0] <= self.max_x
                and self.min_y <= pos[1] <= self.max_y
            ):
                hit_target = True
        return traj, hit_target

    def solve_part_1(self):
        max_alt = 0
        for x in range(1000):
            for y in range(1000):
                traj, hit_target = self.compute_traj(x, y)
                if hit_target:
                    max_alt = max(max_alt, max(traj, key=lambda x: x[1])[1])
        answer = max_alt
        print(answer)
        return answer

    def solve_part_2(self):
        num_hits = 0
        for x in range(1000):
            for y in range(-1000, 1000, 1):
                traj, hit_target = self.compute_traj(x, y)
                if hit_target:
                    num_hits += 1
        answer = num_hits
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
