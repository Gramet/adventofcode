def is_valid_num(line):
    requirements = line.split()[0]
    min = int(requirements.split('-')[0])
    max = int(requirements.split('-')[1])
    char = line.split()[1][0]
    pwd = line.split()[2]

    count = pwd.count(char)
    if count >= min and count <= max:
        return True
    else:
        return False

def is_valid_pos(line):
    requirements = line.split()[0]
    pos1 = int(requirements.split('-')[0]) - 1
    pos2 = int(requirements.split('-')[1]) - 1
    char = line.split()[1][0]
    pwd = line.split()[2]

    if (pwd[pos1] == char) ^ (pwd[pos2] == char):
        return True
    else:
        return False


with open('day2_input', 'r') as f:
   lines = f.readlines()

count = 0
for line in lines:
   s = line
   if is_valid_num(s):
       count +=1
   
print(f"{count} valid passwords")

count = 0
for line in lines:
   s = line
   if is_valid_pos(s):
       count +=1

print(f"{count} valid passwords")
