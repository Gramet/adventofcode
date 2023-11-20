from copy import deepcopy
from functools import lru_cache
from pathlib import Path

from aoc_utils import read_input

INPUT_FILE = Path(__file__).parent / "sample"
from aoc_utils import manhattan_distance, shortest_path

target_cols = {"A": 3, "B": 5, "C": 7, "D": 9}


def early_exit(pos_to_eval, visited, current_best, **kwargs):
    current_map, current_cost = pos_to_eval[0], pos_to_eval[1]
    if current_cost >= current_best:
        return True
    if (
        tuple(current_map.items()) in visited
        and current_cost >= visited[tuple(current_map.items())]
    ):
        return True
    if current_best <= current_cost + get_min_expected_cost(current_map):
        return True
    return False


def get_min_expected_cost(current_map):
    cost = 0
    for pos, val in current_map.items():
        if val in target_cols and pos[1] != target_cols[val]:
            cost += get_move_cost(pos, (2, target_cols[val]), val)
    return cost


def reach_target(pos_to_eval, target_pos, **kwargs):
    current_map = pos_to_eval[0]
    if current_map == target_pos:
        return True
    return False


def get_next_states(pos_to_eval, graph, visited, **kwargs) -> list:
    current_map, current_cost = pos_to_eval[0], pos_to_eval[1]
    next_possible_moves = get_next_possible_moves(current_map, graph)
    results = []
    for next_move in next_possible_moves:
        next_map = deepcopy(current_map)
        start, end = next_move
        next_map[start] = current_map[end]
        next_map[end] = current_map[start]
        move_cost = get_move_cost(start, end, current_map[start])

        if (
            tuple(next_map.items()) in visited
            and current_cost + move_cost >= visited[tuple(next_map.items())]
        ):
            continue

        results.append((next_map, current_cost + move_cost))
    return results


def update_visited(visited, pos_to_eval, **kwargs):
    current_map, current_cost = pos_to_eval[0], pos_to_eval[1]
    visited[tuple(current_map.items())] = current_cost


def update_current_best(current_best, pos_to_eval, **kwargs):
    current_cost = pos_to_eval[1]
    print(f"Found a solution with cost {current_cost}")
    return min(current_cost, current_best)


def get_next_possible_moves(current_map, graph):
    next_possible_moves = []
    for start, val in [(pos, val) for pos, val in current_map.items() if val in "ABCD"]:
        for end in graph[val][start]:
            if current_map[end] == "." and path_is_free(start, end, current_map):
                next_possible_moves.append((start, end))

    return next_possible_moves


@lru_cache
def get_move_cost(start, end, val):
    cost_map = {"A": 1, "B": 10, "C": 100, "D": 1000}
    if start[1] == end[1]:
        # same column
        return manhattan_distance(start, end) * cost_map[val]
    else:
        # different column, need to go through first row
        return ((start[0] - 1) + (end[0] - 1) + abs(start[1] - end[1])) * cost_map[val]


def path_is_free(start, end, current_map):
    if start[1] == end[1]:
        # same column
        dist = abs(start[0] - end[0])
        for d in range(1, dist):
            if current_map[(min(start[0], end[0]) + d, start[1])] != ".":
                return False
    else:
        # different column
        for row in range(2, start[0]):
            if current_map[(row, start[1])] != ".":
                return False
        for col in range(min(start[1], end[1]), max(start[1], end[1])):
            if (1, col) not in current_map or (1, col) == start or (1, col) == end:
                continue
            if current_map[(1, col)] != ".":
                return False
        for row in range(2, end[0]):
            if current_map[(row, end[1])] != ".":
                return False
    if end[0] > 1:
        # If going in a column, it must be only the same letters
        depth = 2
        while True:
            if (depth, end[1]) not in current_map:
                break
            if current_map[(depth, end[1])] not in f".{current_map[start]}":
                return False
            depth += 1
    return True


def prettyprint(current_map):
    print("#############")
    print(
        "#"
        + "".join(
            [
                current_map[(1, x)] if (1, x) in current_map else "."
                for x in range(1, 12)
            ]
        )
        + "#"
    )
    print(
        "###"
        + current_map[(2, 3)]
        + "#"
        + current_map[(2, 5)]
        + "#"
        + current_map[(2, 7)]
        + "#"
        + current_map[(2, 9)]
        + "###"
    )
    print(
        "  #"
        + current_map[(3, 3)]
        + "#"
        + current_map[(3, 5)]
        + "#"
        + current_map[(3, 7)]
        + "#"
        + current_map[(3, 9)]
        + "#  "
    )
    print("  #########  ")


class Solution:
    def __init__(self):
        self.input = read_input(INPUT_FILE)
        self.map_dict = {}
        for r, line in enumerate(self.input):
            for c, char in enumerate(line.strip("\n")):
                if char in "ABCD." and not (r == 1 and c in [3, 5, 7, 9]):
                    self.map_dict[(r, c)] = char

        self.graph_move = {
            col: {
                k: [
                    k2
                    for k2 in self.map_dict
                    if k != k2
                    and (
                        (
                            k[0] == 1 and k2[1] == target_col
                        )  # from topline to target col
                        or (k[0] != 1 and k2[0] == 1)  # from col to topline
                        or (
                            k2[1] == target_col and k[1] != target_col
                        )  # from col to target_col
                    )
                ]
                for k in self.map_dict
            }
            for col, target_col in target_cols.items()
        }
        prettyprint(self.map_dict)

    def solve_part_1(self):
        target_map_dict = {
            (1, 1): ".",
            (1, 2): ".",
            (1, 4): ".",
            (1, 6): ".",
            (1, 8): ".",
            (1, 10): ".",
            (1, 11): ".",
            (2, 3): "A",
            (2, 5): "B",
            (2, 7): "C",
            (2, 9): "D",
            (3, 3): "A",
            (3, 5): "B",
            (3, 7): "C",
            (3, 9): "D",
        }
        start_pos = self.map_dict
        start_cost = 0
        current_best = 1e100
        current_pos = [(start_pos, start_cost)]

        answer = shortest_path(
            starting_positions=current_pos,
            visited={},
            early_exit=early_exit,
            get_next_states=get_next_states,
            reach_target=reach_target,
            update_visited=update_visited,
            update_current_best=update_current_best,
            current_best=current_best,
            target_pos=target_map_dict,
            graph=self.graph_move,
        )

        print(f"Part 1: {answer}")
        return answer

    def solve_part_2(self):
        self.input = read_input(Path(__file__).parent / "input_part2")
        self.map_dict = {}
        for r, line in enumerate(self.input):
            for c, char in enumerate(line.strip("\n")):
                if char in "ABCD." and not (r == 1 and c in [3, 5, 7, 9]):
                    self.map_dict[(r, c)] = char

        self.graph_move = {
            col: {
                k: [
                    k2
                    for k2 in self.map_dict
                    if k != k2
                    and (
                        (
                            k[0] == 1 and k2[1] == target_col
                        )  # from topline to target col
                        or (k[0] != 1 and k2[0] == 1)  # from col to topline
                        or (
                            k2[1] == target_col and k[1] != target_col
                        )  # from col to target_col
                    )
                ]
                for k in self.map_dict
            }
            for col, target_col in target_cols.items()
        }

        target_map_dict = {
            (1, 1): ".",
            (1, 2): ".",
            (1, 4): ".",
            (1, 6): ".",
            (1, 8): ".",
            (1, 10): ".",
            (1, 11): ".",
            (2, 3): "A",
            (2, 5): "B",
            (2, 7): "C",
            (2, 9): "D",
            (3, 3): "A",
            (3, 5): "B",
            (3, 7): "C",
            (3, 9): "D",
            (4, 3): "A",
            (4, 5): "B",
            (4, 7): "C",
            (4, 9): "D",
            (5, 3): "A",
            (5, 5): "B",
            (5, 7): "C",
            (5, 9): "D",
        }
        start_pos = self.map_dict
        start_cost = 0
        current_best = 1e100
        current_pos = [(start_pos, start_cost)]

        answer = shortest_path(
            starting_positions=current_pos,
            visited={},
            early_exit=early_exit,
            get_next_states=get_next_states,
            reach_target=reach_target,
            update_visited=update_visited,
            update_current_best=update_current_best,
            current_best=current_best,
            target_pos=target_map_dict,
            graph=self.graph_move,
        )

        print(f"Part 2: {answer}")
        return answer

    def save_results(self):
        with open(Path(__file__).parent / "part1", "w") as opened_file:
            opened_file.write(str(self.solve_part_1()))

        with open(Path(__file__).parent / "part2", "w") as opened_file:
            opened_file.write(str(self.solve_part_2()))


if __name__ == "__main__":
    solution = Solution()
    solution.save_results()
