from pathlib import Path


class Solution:
    def __init__(self):
        with open(Path(__file__).parent / "input", "r") as f:
            self.input = f.readlines()
        self.map = {}
        for line in self.input:
            cave1, cave2 = line.strip("\n").split("-")
            self.map[cave1] = self.map.get(cave1, []) + [cave2]
            self.map[cave2] = self.map.get(cave2, []) + [cave1]

    def solve_part_1(self):
        queue = [("start",)]
        paths = set()
        while queue:
            cur_path = queue.pop(0)
            cur_node = cur_path[-1]
            if cur_node == "end":
                paths.add(cur_path)
                continue
            for neighbour in self.map[cur_node]:
                if neighbour.isupper() or (
                    neighbour.islower() and neighbour not in cur_path
                ):
                    queue.append(cur_path + (neighbour,))

        answer = len(paths)
        print(answer)
        return answer

    def solve_part_2(self):
        queue = [("start",)]
        paths = set()
        small_caves = set(
            [k for k in self.map if k.islower() and k not in ["start", "end"]]
        )
        while queue:
            cur_path = queue.pop(0)
            cur_node = cur_path[-1]
            if cur_node == "end":
                paths.add(cur_path)
                continue
            for neighbour in self.map[cur_node]:
                if (
                    neighbour.isupper()
                    or neighbour == "end"
                    or (
                        neighbour in small_caves
                        and (
                            cur_path.count(neighbour) == 0
                            or max(cur_path.count(cave) for cave in small_caves) <= 1
                        )
                    )
                ):
                    queue.append(cur_path + (neighbour,))

        answer = len(paths)
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
