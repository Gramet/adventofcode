from pathlib import Path

from aoc_utils import *

INPUT_FILE = Path(__file__).parent / "input"


class Solution:
    def __init__(self):
        self.input = read_input(INPUT_FILE)
        self.graph = defaultdict(list)
        for line in self.input:
            nodes = parse_words(line)
            for dest in nodes[1:]:
                self.graph[nodes[0]].append(dest)

    def solve_part_1(self):
        answer = len(self.get_paths("you", "out"))
        print(answer)
        return answer

    def get_paths(self, start, target):
        paths = [[start]]
        complete_paths = []
        while paths:
            path = paths.pop()
            last_node = path[-1]
            if last_node == target:
                complete_paths.append(path)
                continue
            for neigh in self.graph[last_node]:
                new_path = path + [neigh]
                paths.append(new_path)
        return complete_paths

    def get_paths2(self, start, target):
        paths = defaultdict(int)
        paths[(start, 1, False, False)] = 1
        last_visited = [(start, 1, False, False)]
        while last_visited:
            new_last_visited = []
            for last_node in last_visited:
                node, path_len, seen_fft, seen_dac = last_node
                if node == "fft":
                    seen_fft = True
                if node == "dac":
                    seen_dac = True
                for neigh in self.graph[node]:
                    state = (neigh, path_len + 1, seen_fft, seen_dac)
                    if state not in paths:
                        new_last_visited.append(state)
                    paths[state] += paths[last_node]
            last_visited = new_last_visited
        return sum(paths[p] for p in paths if p[0] == target and p[2] and p[3])

    def solve_part_2(self):
        answer = self.get_paths2("svr", "out")
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
