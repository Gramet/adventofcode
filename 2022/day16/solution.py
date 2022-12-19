from pathlib import Path
from copy import deepcopy
from tqdm import tqdm


class Solution:
    def __init__(self):
        with open(Path(__file__).parent / "input", "r") as f:
            self.input = f.readlines()
        self.valves = {}
        for line in self.input:
            valve = line.split(" has")[0][6:8]
            flow_rate = int(line.split("=")[1].split(";")[0])
            try:
                tunnels = line.strip().split("valves ")[1].split(", ")
            except:
                tunnels = [line.strip().split("valve ")[1]]
            self.valves[valve] = {"flow": flow_rate, "tunnels": tunnels, "paths": {}}
        self.need_opening = set([k for k in self.valves if self.valves[k]["flow"]])
        self.tot_flow = sum(self.valves[k]["flow"] for k in self.need_opening)

        for k in tqdm(self.need_opening.union(set(["AA"]))):
            for k2 in self.need_opening:
                if k == k2:
                    continue
                self.valves[k]["paths"][k2] = self.shortest_path(k, k2)

    def shortest_path(self, start, end):
        depth = 1
        visible_at_d = set(self.valves[start]["tunnels"])
        if end in visible_at_d:
            return depth
        else:
            visited = deepcopy(visible_at_d)
            new_visibles = deepcopy(visible_at_d)
            while True:
                depth += 1
                for valve in new_visibles:
                    visible_at_d = visible_at_d.union(
                        set(self.valves[valve]["tunnels"])
                    )
                new_visibles = visible_at_d.difference(visited)
                visited = visited.union(new_visibles)
                if end in new_visibles:
                    return depth

    def best_path(self, point, time_left, opened, score, path):
        path["-".join(opened)] = max(path.get("".join(opened), 0), score)
        for valve in self.valves[point]["paths"]:
            time_left_after_valve = (
                time_left - self.valves[point]["paths"][valve] - 1
            )  # 1 to open the valve
            if time_left_after_valve <= 0 or valve in opened:
                continue
            self.best_path(
                valve,
                time_left_after_valve,
                opened + [valve],
                score + time_left_after_valve * self.valves[valve]["flow"],
                path,
            )
        return path

    def solve_part_1(self):
        start = "AA"
        time_left = 30
        opened = []
        score = 0
        path = {}
        answer = self.best_path(start, time_left, opened, score, path)
        print(max(answer, key=answer.get))
        answer = max(answer.values())
        # print(max(list(answer.items()), lambda x: x[1]))
        print(answer)
        return answer

    def solve_part_2(self):
        start = "AA"
        time_left = 26
        opened = []
        score = 0
        path = {}
        answer = self.best_path(start, time_left, opened, score, path)
        # Graph is disjoint in AA so we can keep the best path + the best that has no common node
        path_1 = max(answer, key=answer.get)
        path_without_common_nodes = {
            k: v
            for k, v in answer.items()
            if len(set(path_1.split("-")).intersection(set(k.split("-")))) == 0
        }

        path_2 = max(path_without_common_nodes, key=path_without_common_nodes.get)

        answer = answer[path_1] + answer[path_2]
        print(path_1, path_2)
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
