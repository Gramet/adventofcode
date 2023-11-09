import heapq
import sys
from pathlib import Path
from string import ascii_letters, ascii_lowercase, ascii_uppercase

sys.setrecursionlimit(100000)

deltas = [(0, 1), (0, -1), (1, 0), (-1, 0)]


def path_from_parents(parents, end):
    out = [end]
    while out[-1] in parents:
        out.append(parents[out[-1]])
    out.reverse()
    return out


class Solution:
    def __init__(self):
        with open(Path(__file__).parent / "input", "r") as f:
            self.input = f.readlines()
            self.input = [line.strip("\n") for line in self.input]
        self.keys = {}
        self.doors = {}
        self.start = []
        for r, row in enumerate(self.input):
            for c, char in enumerate(row):
                if char in ascii_lowercase:
                    self.keys[char] = (r, c)
                elif char in ascii_uppercase:
                    self.doors[char] = (r, c)
                elif char == "@":
                    self.start.append((r, c))

    def compute_paths(self, current_positions, paths_found):
        current_positions = sorted(current_positions, key=lambda x: x[1])
        next_pos = current_positions.pop(0)
        char = self.input[next_pos[0][0]][next_pos[0][1]]
        if char == "." or char == "@":
            for delta in deltas:
                pos_tuple = (next_pos[0][0] + delta[0], next_pos[0][1] + delta[1])
                if pos_tuple not in self.visited:
                    new_pos = (
                        pos_tuple,
                        next_pos[1] + 1,
                        next_pos[2],
                    )
                    current_positions.append(new_pos)
                    self.visited.update({pos_tuple})

        elif char in ascii_lowercase:
            if char not in paths_found:
                paths_found[char] = (next_pos[1], next_pos[2])
            for delta in deltas:
                pos_tuple = (next_pos[0][0] + delta[0], next_pos[0][1] + delta[1])
                if pos_tuple not in self.visited:
                    new_pos = (
                        pos_tuple,
                        next_pos[1] + 1,
                        next_pos[2],
                    )
                    current_positions.append(new_pos)
                    self.visited.update({pos_tuple})

        elif char in ascii_uppercase:
            for delta in deltas:
                pos_tuple = (next_pos[0][0] + delta[0], next_pos[0][1] + delta[1])
                if pos_tuple not in self.visited:
                    new_pos = (
                        pos_tuple,
                        next_pos[1] + 1,
                        next_pos[2].union({char}),
                    )
                    current_positions.append(new_pos)
                    self.visited.update({pos_tuple})

        if len(paths_found) == len(self.keys) or len(current_positions) == 0:
            return paths_found
        return self.compute_paths(current_positions, paths_found)

    def search_nodes(self, start_node, keys_obtained, cost=0):
        seen = set()
        costs = {start_node: 0}
        queue = [(cost, (start_node, keys_obtained))]
        parents = {}
        while queue:
            cost, node = heapq.heappop(queue)
            if node in seen:
                continue
            if len(node[1]) == len(self.keys):
                break
            seen.add(node)

            for next_key, path_ in self.paths[node[0]].items():
                if (
                    next_key not in node[1]
                    and next_key != node[0]
                    and all(
                        required_key.lower() in node[1] for required_key in path_[1]
                    )
                ):
                    next_cost = cost + path_[0]
                    next_node = (next_key, node[1].union(frozenset({next_key})))
                    if next_node not in costs or next_cost <= costs[next_node]:
                        costs[next_node] = next_cost
                        heapq.heappush(queue, (next_cost, next_node))
                        parents[next_node] = node

        return cost, [n[0] for n in path_from_parents(parents, node)]

    def search_nodes_multi(self, start_node, keys_obtained, cost=0):
        seen = set()
        costs = {start_node: 0}
        queue = [(cost, (start_node, keys_obtained))]
        parents = {}
        while queue:
            cost, node = heapq.heappop(queue)
            if node in seen:
                continue
            if len(node[1]) == len(self.keys):
                break
            seen.add(node)

            for robot_idx, robot_pos in enumerate(node[0]):
                for next_key, path_ in self.paths[robot_pos].items():
                    if (
                        next_key not in node[1]
                        and next_key not in node[0]
                        and all(
                            required_key.lower() in node[1] for required_key in path_[1]
                        )
                    ):
                        next_cost = cost + path_[0]
                        next_node = (
                            tuple(
                                x if idx != robot_idx else next_key
                                for idx, x in enumerate(node[0])
                            ),
                            node[1].union(frozenset({next_key})),
                        )
                        if next_node not in costs or next_cost <= costs[next_node]:
                            costs[next_node] = next_cost
                            heapq.heappush(queue, (next_cost, next_node))
                            parents[next_node] = node

        return cost, [n[0] for n in path_from_parents(parents, node)]

    def solve_part_1(self):
        self.paths = {}
        self.visited = set([])
        self.paths["@"] = self.compute_paths(
            current_positions=[(self.start[0], 0, set([]))], paths_found=dict()
        )
        for char in self.keys:
            self.visited = set([])
            self.paths[char] = self.compute_paths(
                current_positions=[(self.keys[char], 0, set([]))], paths_found=dict()
            )
        max_cost = self.search_nodes(
            "@",
            frozenset(),
        )
        answer = max_cost[0]
        print(answer)
        return answer

    def solve_part_2(self):
        with open(Path(__file__).parent / "input2", "r") as f:
            self.input = f.readlines()
            self.input = [line.strip("\n") for line in self.input]
        self.keys = {}
        self.doors = {}
        self.start = []
        for r, row in enumerate(self.input):
            for c, char in enumerate(row):
                if char in ascii_lowercase:
                    self.keys[char] = (r, c)
                elif char in ascii_uppercase:
                    self.doors[char] = (r, c)
                elif char == "@":
                    self.start.append((r, c))

        self.paths = {}
        self.visited = set([])
        for idx, start in enumerate(self.start):
            self.paths[f"@{idx}"] = self.compute_paths(
                current_positions=[(start, 0, set([]))],
                paths_found=dict(),
            )
        for char in self.keys:
            self.visited = set([])
            self.paths[char] = self.compute_paths(
                current_positions=[(self.keys[char], 0, set([]))], paths_found=dict()
            )
        max_cost = self.search_nodes_multi(
            ("@0", "@1", "@2", "@3"),
            frozenset(),
        )
        answer = max_cost[0]
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
