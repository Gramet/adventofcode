from pathlib import Path

REQUIRED_KEYS = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]
ALL_KEYS = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid", "cid"]

HCL_CHAR = [
    "0",
    "1",
    "2",
    "3",
    "4",
    "5",
    "6",
    "7",
    "8",
    "9",
    "a",
    "b",
    "c",
    "d",
    "e",
    "f",
]
ECL_VAL = ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]
NUMS = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]


def check_data(d):
    if int(d["byr"]) < 1920 or int(d["byr"]) > 2002:
        return False

    if int(d["iyr"]) < 2010 or int(d["iyr"]) > 2020:
        return False

    if int(d["eyr"]) < 2020 or int(d["eyr"]) > 2030:
        return False

    if (len(d["hgt"]) not in ([4, 5])) or not (all(x in NUMS for x in d["hgt"][:-2])):
        return False

    if d["hgt"][-2:] == "cm":
        if int(d["hgt"][:-2]) < 150 or int(d["hgt"][:-2]) > 193:
            return False
    elif d["hgt"][-2:] == "in":
        if int(d["hgt"][:-2]) < 59 or int(d["hgt"][:-2]) > 76:
            return False
    else:
        print("hgt", d["hgt"])
        return False

    if (
        len(d["hcl"]) != 7
        or d["hcl"][0] != "#"
        or not (all(x in HCL_CHAR for x in d["hcl"][1:7]))
    ):
        return False

    if d["ecl"] not in ECL_VAL:
        return False

    if len(d["pid"]) != 9 or not (all(x in NUMS for x in d["pid"])):
        return False

    return True


def has_all_fields(passport_lines):
    d = {}
    for line in passport_lines:
        infos = line.split(" ")
        for info in infos:
            k = info.split(":")[0]
            v = info.split(":")[1]
            d[k] = v.strip("\n")

    for k in REQUIRED_KEYS:
        if k not in d:
            return False
    return True


def is_valid(passport_lines):
    d = {}
    for line in passport_lines:
        infos = line.split(" ")
        for info in infos:
            k = info.split(":")[0]
            v = info.split(":")[1]
            d[k] = v.strip("\n")

    for k in REQUIRED_KEYS:
        if k not in d:
            return False

    return check_data(d)


class Solution:
    def __init__(self):
        with open(Path(__file__).parent / "input", "r") as f:
            self.input = f.readlines()

        total_buff = []
        buff = []
        for line in self.input:
            if line == "\n":
                total_buff.append(buff)
                buff = []
            else:
                buff.append(line)
        total_buff.append(buff)
        self.input = total_buff

    def solve_part_1(self):
        answer = sum(has_all_fields(x) for x in self.input)
        print(answer)
        return answer

    def solve_part_2(self):
        answer = sum(is_valid(x) for x in self.input)
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
