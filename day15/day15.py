from collections import defaultdict
with open('input', 'r') as f:
    lines = f.readlines()

starts = [int(x) for x in lines[0].split(',')]
print(starts)

l = starts
d = defaultdict(lambda: t)
lastnum = -1
for t, num in enumerate(starts):
    d[lastnum], lastnum = t, int(num)
for t in range(len(starts), 30000000):
    d[lastnum], lastnum = t, t-d[lastnum]

print(t+1, lastnum)#, d_cop, d)

