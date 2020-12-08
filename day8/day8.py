with open('input_fixed', 'r') as f:
   lines = f.readlines()

def compute(lines):
    list_passed = []
    acc = 0
    ind = 0
    while (ind not in list_passed) and (ind < len(lines)):
        list_passed.append(ind)
        line = lines[ind]
        instr = line.split(' ')[0]
        val = int(line.split(' ')[1])
        if instr == 'nop':
            ind += 1
        elif instr == 'acc':
            acc += val
            ind += 1
        elif instr == 'jmp':
            ind += val
    if ind >= len(lines):
        return acc, True, list_passed
    return acc, False, list_passed

acc, exited, list_passed = compute(lines)
print(list_passed)
print(acc, exited)

for ind, line in enumerate(lines):
    val = int(line.split(' ')[1])
    instr = line.split(' ')[0]
    if instr == 'nop':
        lines[ind] = '{} {}'.format('jmp', val)
        acc, ret, list_passed = compute(lines)
        if ret:
            print(ind, acc)
            break
        lines[ind] = '{} {}'.format('nop', val)
    if instr == 'jmp':
        lines[ind] = '{} {}'.format('nop', val)
        acc, ret, list_passed = compute(lines)
        if ret:
            print('jmp')
            print(list_passed)
            print(ind, acc)
            break
        lines[ind] = '{} {}'.format('jmp', val)

