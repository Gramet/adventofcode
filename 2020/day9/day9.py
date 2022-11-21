with open("input", "r") as f:
    lines = f.readlines()


def two_sum(l, target):
    s = set(l)
    for num in l:
        diff = target - num
        if diff in s:
            return diff * num
    return None


nums = []
for ind, l in enumerate(lines):
    nums.append(int(l))
    if ind <= 24:
        continue
    else:
        if two_sum(nums[:25], nums[25]) is None:
            print(nums[25])
            break
        nums.pop(0)


nums = []
ind = 0
for ind, l in enumerate(lines):
    nums.append(int(l))
    while sum(nums) > 70639851:
        nums.pop(0)

    if sum(nums) == 70639851:
        print(max(nums) + min(nums))
        break
