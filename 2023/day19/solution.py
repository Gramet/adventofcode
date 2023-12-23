from copy import deepcopy
from pathlib import Path

from aoc_utils import *

INPUT_FILE = Path(__file__).parent / "input"


def invert_condition(cond):
    if "<" in cond:
        cond = cond.replace("NOT-", "").replace("<", ">=")
    elif ">" in cond:
        cond = cond.replace("NOT-", "").replace(">", "<=")
    return cond


class Solution:
    def __init__(self):
        self.workflows, self.parts = read_input_parts(INPUT_FILE)
        self.work_dict = {}
        for workflow in self.workflows.split("\n"):
            name, workflow = workflow.strip().split("{")
            workflow = workflow.replace("}", "").split(",")
            self.work_dict[name] = workflow

    def check_workflow(self, part_dict, name):
        workflow = self.work_dict[name]
        for step in workflow:
            if step == "A":
                return sum(part_dict.values())
            elif step == "R":
                return 0
            elif ":" not in step:
                return self.check_workflow(part_dict, step)
            else:
                check, res = step.split(":")
                key = check[0]
                op = check[1]
                comp = int(check[2:])
                if (
                    op == ">"
                    and part_dict[key] > comp
                    or op == "<"
                    and part_dict[key] < comp
                ):
                    if res == "A":
                        return sum(part_dict.values())
                    elif res == "R":
                        return 0
                    else:
                        return self.check_workflow(part_dict, res)

    def solve_part_1(self):
        answer = 0
        for part in self.parts.splitlines():
            x, m, a, s = parse_ints(part)
            part_dict = {"x": x, "m": m, "a": a, "s": s}
            answer += self.check_workflow(part_dict, "in")

        print(answer)
        return answer

    def solve_part_2(self):
        # Compute all workflows that lead to acceptance
        total_accepted_wf = []
        list_to_check = [(self.work_dict["in"], tuple())]
        while list_to_check:
            next_wf, cond_to_reach = list_to_check.pop()
            for step_num, step in enumerate(next_wf):
                cur_cond_to_reach = cond_to_reach
                if "A" in step:
                    if ":" in step:
                        cur_cond_to_reach = cur_cond_to_reach + (step.split(":")[0],)
                    for i in range(step_num):
                        cur_cond_to_reach += (
                            invert_condition(next_wf[i].split(":")[0]),
                        )
                    total_accepted_wf.append(cur_cond_to_reach)
                elif "R" in step:
                    continue
                else:
                    for i in range(step_num):
                        cur_cond_to_reach += (
                            invert_condition(next_wf[i].split(":")[0]),
                        )
                    if ":" in step:
                        cur_cond_to_reach = cur_cond_to_reach + (step.split(":")[0],)
                        list_to_check.append(
                            (self.work_dict[step.split(":")[1]], cur_cond_to_reach)
                        )
                    else:
                        list_to_check.append((self.work_dict[step], cur_cond_to_reach))

        # Simplify inequalities for each workflow to compute the number of possible tuples
        answer = 0
        for cond in total_accepted_wf:
            bounds = {"x": [1, 4000], "m": [1, 4000], "a": [1, 4000], "s": [1, 4000]}
            for step in cond:
                key = step[0]
                if ">=" in step:
                    bounds[key][0] = max(int(step[3:]), bounds[key][0])
                elif "<=" in step:
                    bounds[key][1] = min(int(step[3:]), bounds[key][1])
                elif ">" in step:
                    bounds[key][0] = max(int(step[2:]) + 1, bounds[key][0])
                elif "<" in step:
                    bounds[key][1] = min(int(step[2:]) - 1, bounds[key][1])
            res = 1
            for key, bound in bounds.items():
                res = res * (bound[1] - bound[0] + 1)
            answer += res

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
