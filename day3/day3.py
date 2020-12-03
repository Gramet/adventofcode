def advance(line, pos=0, right=3):
    pos = (pos + right) % 31
    is_tree = True if line[pos] == '#' else False

    if is_tree:
        return 1, pos
    else:
        return 0, pos    

with open('day3_input', 'r') as f:
   lines = f.readlines()

def go_down(lines, down=1, right=3):

    count = 0
    pos = 0
    for num_line, line in enumerate(lines):
        if num_line % down != 0 or num_line == 0:
            continue
        s = line
        hit_tree, pos = advance(s, pos, right)
        count += hit_tree

    return count

print(go_down(lines, 1,1))
print(go_down(lines, 1,3))
print(go_down(lines, 1,5))
print(go_down(lines, 1,7))
print(go_down(lines, 2,1))

res = go_down(lines, 1,1)
res *= go_down(lines, 1,3)
res *= go_down(lines, 1,5)
res *= go_down(lines, 1,7)
res *= go_down(lines, 2,1)

print(res)