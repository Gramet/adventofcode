import json

def two_sum(l, target):
    s = set(l)
    for num in l:
        diff = target - num
        if diff in s:
            print(diff, num, diff+num)
            return diff * num
    return None

def three_sum(l, target):
    s = set(l)
    for idx, num in enumerate(l):
        diff = target - num
        two_sum_res = two_sum(l[:idx] + l[idx+1:], diff)
        if two_sum_res is not None:
            print(num, two_sum_res)
            return num * two_sum_res
    return None


with open('day1_input.json', 'r') as f:
    l = json.load(f)

print(two_sum(l, 2020))
print(three_sum(l, 2020))
