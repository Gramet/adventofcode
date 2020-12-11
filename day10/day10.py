import collections
with open('input', 'r') as f:
   lines = f.readlines()

adapters = sorted([int(line) for line in lines])
adapters.insert(0,0)
adapters.append(max(adapters) + 3)
print(adapters[0])
s1 = 0
s3 = 0
for i in range(1, len(adapters)):
    diff = adapters[i] - adapters[i-1]
    if diff == 1:
        s1 += 1
    elif diff == 3:
        s3 += 1

print(s1 * s3)

num_pos = 1
cache = collections.defaultdict(int, {0: 1})

for jolt in adapters:
	for possible in (jolt - 1, jolt - 2, jolt - 3):
		if possible in cache:
			cache[jolt] += cache[possible]

print(cache[adapters[-1]])