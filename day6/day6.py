def count_yes(group):
    s = set([])
    for person in group:
        s = s | set(person)
    return len(s)

def count_all_yes(group):
    s = set(group[0])
    for person in group:
        s = s & set(person)
    return len(s)

with open('day6_input', 'r') as f:
   lines = f.readlines()

buff = []
sum_yes = 0
sum_all_yes = 0
for line in lines:
    if line == '\n':
        sum_all_yes += count_all_yes(buff)
        sum_yes += count_yes(buff)
        buff = []
    else:
        buff.append(line.strip('\n'))

sum_yes += count_yes(buff)
sum_all_yes += count_all_yes(buff)

print(sum_yes)
print(sum_all_yes)