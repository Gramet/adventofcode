import re
from copy import deepcopy
from math import ceil
from pathlib import Path

ORE = 0
CLAY = 1
OBSIDIAN = 2
GEODE = 3


def eval_blueprint(blueprint, time_left, robots, items, answer, score):
    state_key = f"{robots}-{items}-{time_left}"
    answer[state_key] = max(answer.get(state_key, 0), score)
    if time_left == 1:
        return answer
    max_reachable = score + time_left * (time_left - 1) / 2
    if max_reachable <= max(answer.values()):
        return answer

    # Build Geode robot
    if robots[OBSIDIAN]:
        geode_cost = blueprint["geode"]
        time_to_build = max(
            ceil((geode_cost[1] - items[OBSIDIAN]) / robots[OBSIDIAN]) + 1,
            ceil((geode_cost[0] - items[ORE]) / robots[ORE]) + 1,
            1,
        )
        if time_to_build < time_left:
            new_time_left = time_left - time_to_build
            new_robots = deepcopy(robots)
            new_items = deepcopy(items)
            new_robots[GEODE] += 1
            new_items[ORE] += time_to_build * robots[ORE] - geode_cost[0]
            new_items[CLAY] += time_to_build * robots[CLAY]
            new_items[OBSIDIAN] += time_to_build * robots[OBSIDIAN] - geode_cost[1]
            new_items[GEODE] += time_to_build * robots[GEODE]

            eval_blueprint(
                blueprint,
                new_time_left,
                new_robots,
                new_items,
                answer,
                score + new_time_left,
            )

    # Build Obsidian robot
    if robots[CLAY] and (robots[OBSIDIAN] < blueprint["geode"][1]):
        obs_cost = blueprint["obsidian"]
        time_to_build = max(
            ceil((obs_cost[1] - items[CLAY]) / robots[CLAY]) + 1,
            ceil((obs_cost[0] - items[ORE]) / robots[ORE]) + 1,
            1,
        )
        if time_to_build < time_left:
            new_time_left = time_left - time_to_build
            new_robots = deepcopy(robots)
            new_items = deepcopy(items)
            new_robots[OBSIDIAN] += 1
            new_items[ORE] += time_to_build * robots[ORE] - obs_cost[0]
            new_items[CLAY] += time_to_build * robots[CLAY] - obs_cost[1]
            new_items[OBSIDIAN] += time_to_build * robots[OBSIDIAN]
            new_items[GEODE] += time_to_build * robots[GEODE]

            eval_blueprint(
                blueprint,
                new_time_left,
                new_robots,
                new_items,
                answer,
                score,
            )

    # Build Clay robot
    if robots[CLAY] < blueprint["obsidian"][1]:
        clay_cost = blueprint["clay"]
        time_to_build = max(ceil((clay_cost - items[ORE]) / robots[ORE]) + 1, 1)
        if time_to_build < time_left:
            new_time_left = time_left - time_to_build
            new_robots = deepcopy(robots)
            new_items = deepcopy(items)
            new_robots[CLAY] += 1
            new_items[ORE] += time_to_build * robots[ORE] - clay_cost
            new_items[CLAY] += time_to_build * robots[CLAY]
            new_items[OBSIDIAN] += time_to_build * robots[OBSIDIAN]
            new_items[GEODE] += time_to_build * robots[GEODE]

            eval_blueprint(
                blueprint,
                new_time_left,
                new_robots,
                new_items,
                answer,
                score,
            )

    # Build Ore robot
    if not (
        robots[ORE]
        >= max(
            [
                blueprint["ore"],
                blueprint["clay"],
                blueprint["obsidian"][0],
                blueprint["geode"][0],
            ]
        )
    ):
        ore_cost = blueprint["ore"]
        time_to_build = max(ceil((ore_cost - items[ORE]) / robots[ORE]) + 1, 1)
        if time_to_build < time_left:
            new_time_left = time_left - time_to_build
            new_robots = deepcopy(robots)
            new_items = deepcopy(items)
            new_robots[ORE] += 1
            new_items[ORE] += time_to_build * robots[ORE] - ore_cost
            new_items[CLAY] += time_to_build * robots[CLAY]
            new_items[OBSIDIAN] += time_to_build * robots[OBSIDIAN]
            new_items[GEODE] += time_to_build * robots[GEODE]
            eval_blueprint(
                blueprint,
                new_time_left,
                new_robots,
                new_items,
                answer,
                score,
            )
    return answer


class Solution:
    def __init__(self):
        with open(Path(__file__).parent / "input", "r") as f:
            self.input = f.readlines()
        self.blueprints = {}
        for line in self.input:
            matches = re.search(
                r"[^0-9]+(\d+)[^0-9]+(\d+)[^0-9]+(\d+)[^0-9]+(\d+)[^0-9]+(\d+)[^0-9]+(\d+)[^0-9]+(\d+)",
                line,
            )
            self.blueprints[matches.group(1)] = {
                "ore": int(matches.group(2)),
                "clay": int(matches.group(3)),
                "obsidian": (int(matches.group(4)), int(matches.group(5))),
                "geode": (int(matches.group(6)), int(matches.group(7))),
            }
        print(self.blueprints)

    def solve_part_1(self):
        tot_quality = 0
        for id, blueprint in self.blueprints.items():
            answer = eval_blueprint(
                blueprint,
                time_left=24,
                robots=[1, 0, 0, 0],
                items=[0, 0, 0, 0],
                answer={},
                score=0,
            )
            max_val = max(answer.values())
            answer = {k: v for k, v in answer.items() if v == max_val}
            print(f"{int(id)}: quality {max_val}")
            tot_quality += int(id) * max_val
        answer = tot_quality
        print(answer)
        return answer

    def solve_part_2(self):
        tot = 1
        for id, blueprint in self.blueprints.items():
            if int(id) not in [1, 2, 3]:
                continue
            answer = eval_blueprint(
                blueprint,
                time_left=32,
                robots=[1, 0, 0, 0],
                items=[0, 0, 0, 0],
                answer={},
                score=0,
            )
            max_val = max(answer.values())
            print(max_val)
            tot *= max_val

        answer = tot
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
