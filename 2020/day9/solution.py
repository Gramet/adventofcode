from pathlib import Path


def two_sum(l, target):
    s = set(l)
    for num in l:
        diff = target - num
        if diff in s:
            return diff * num
    return None


class Solution:
    def __init__(self):
        with open(Path(__file__).parent / "input", "r") as f:
            self.input = f.readlines()

    def solve_part_1(self):
        nums = []
        for ind, l in enumerate(self.input):
            nums.append(int(l))
            if ind <= 24:
                continue
            else:
                if two_sum(nums[:25], nums[25]) is None:
                    answer = nums[25]
                    break
            nums.pop(0)
        self.step_1_answer = answer
        print(answer)
        return answer

    def solve_part_2(self):
        nums = []
        for l in self.input:
            nums.append(int(l))
            while sum(nums) > self.step_1_answer:
                nums.pop(0)

            if sum(nums) == self.step_1_answer:
                answer = max(nums) + min(nums)
                break
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
