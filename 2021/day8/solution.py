from collections import Counter
from pathlib import Path


class Solution:
    def __init__(self):
        with open(Path(__file__).parent / "input", "r") as f:
            self.input = f.readlines()

    def solve_part_1(self):
        answer = 0
        for line in self.input:
            outputs = line.split(" | ")[1].strip("\n").split(" ")
            for out in outputs:
                if len(out) in [2, 3, 4, 7]:
                    answer += 1

        print(answer)
        return answer

    def solve_part_2(self):
        answer = 0
        for line in self.input:
            input_line = line.split(" | ")[0].strip("\n")
            inputs = line.split(" | ")[0].strip("\n").split(" ")
            outputs = line.split(" | ")[1].strip("\n").split(" ")
            one_str = [x for x in inputs if len(x) == 2][0]
            seven_str = [x for x in inputs if len(x) == 3][0]
            four_str = [x for x in inputs if len(x) == 4][0]
            a_segment = [x for x in seven_str if x not in one_str][0]
            count = Counter(input_line)
            e_segment = [k for k, v in count.items() if v == 4][0]
            b_segment = [k for k, v in count.items() if v == 6][0]
            f_segment = [k for k, v in count.items() if v == 9 and k != " "][0]
            c_segment = [k for k, v in count.items() if v == 8 and k != a_segment][0]
            d_segment = [k for k, v in count.items() if v == 7 and k in four_str][0]
            g_segment = [k for k, v in count.items() if v == 7 and k not in four_str][0]

            zero_str = "".join(
                sorted(
                    [a_segment, b_segment, c_segment, e_segment, f_segment, g_segment]
                )
            )
            one_str = "".join(sorted([c_segment, f_segment]))
            two_str = "".join(
                sorted([a_segment, c_segment, d_segment, e_segment, g_segment])
            )
            three_str = "".join(
                sorted([a_segment, c_segment, d_segment, f_segment, g_segment])
            )
            four_str = "".join(sorted([b_segment, c_segment, d_segment, f_segment]))
            five_str = "".join(
                sorted([a_segment, b_segment, d_segment, f_segment, g_segment])
            )
            six_str = "".join(
                sorted(
                    [a_segment, b_segment, d_segment, e_segment, f_segment, g_segment]
                )
            )
            seven_str = "".join(sorted([a_segment, c_segment, f_segment]))
            eight_str = "".join(
                sorted(
                    [
                        a_segment,
                        b_segment,
                        c_segment,
                        d_segment,
                        e_segment,
                        f_segment,
                        g_segment,
                    ]
                )
            )
            nine_str = "".join(
                sorted(
                    [a_segment, b_segment, c_segment, d_segment, f_segment, g_segment]
                )
            )

            seg_dict = {
                zero_str: "0",
                one_str: "1",
                two_str: "2",
                three_str: "3",
                four_str: "4",
                five_str: "5",
                six_str: "6",
                seven_str: "7",
                eight_str: "8",
                nine_str: "9",
            }
            out_str = ""
            for out in outputs:
                out_str += seg_dict["".join(sorted(out))]
            answer += int(out_str)

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
