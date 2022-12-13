from pathlib import Path


def is_ordered(left, right):
    if isinstance(left, list) and isinstance(right, list):
        for ell, elr in zip(left, right):
            if is_ordered(ell, elr) == False:
                return False
            elif is_ordered(ell, elr) == True:
                return True
        if len(left) < len(right):
            return True
        elif len(left) > len(right):
            return False
    elif isinstance(left, list) and not isinstance(right, list):
        return is_ordered(left, [right])
    elif not isinstance(left, list) and isinstance(right, list):
        return is_ordered([left], right)
    else:
        if left < right:
            return True
        elif right < left:
            return False


class Solution:
    def __init__(self):
        with open(Path(__file__).parent / "input", "r") as f:
            self.input = f.read().split("\n\n")
            self.all_packets = "\n".join(self.input).split("\n")
            print(self.all_packets)

    def solve_part_1(self):
        answer = 0
        for i, pair in enumerate(self.input):
            left, right = pair.split("\n")
            left = eval(left)
            right = eval(right)
            if is_ordered(left, right):
                answer += i + 1

        print(answer)
        return answer

    def solve_part_2(self):
        divider1 = [[2]]
        divider2 = [[6]]
        divider1_idx = 1
        divider2_idx = 1
        for packet in self.all_packets:
            packet = eval(packet)
            if is_ordered(packet, divider1):
                divider1_idx += 1
            if is_ordered(packet, divider2):
                divider2_idx += 1

        answer = divider1_idx * (1 + divider2_idx)
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
