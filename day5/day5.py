
val_dict = {'F':0, 'B':1, 'R':1, 'L':0}

def get_seat(line):
    row = 0
    col = 0
    for i, chr in enumerate(line[:7]):
        row += 2**(6-i) * val_dict[chr]
    for i, chr in enumerate(line[7:]):
        col += 2**(2-i) * val_dict[chr]
    seat_id = row * 8 + col
    return row, col, seat_id

with open('day5_input', 'r') as f:
   lines = f.readlines()

rows = []
cols = []
seats_id = []
for line in lines:
    row, col, seat_id = get_seat(line.strip('\n'))
    rows.append(row)
    cols.append(col)
    seats_id.append(seat_id)

print(f"Max seat id: {max(seats_id)}")
seats_id = sorted(seats_id)

for i, s in enumerate(seats_id[:-1]):
    if (seats_id[i+1] - s) != 1:
        print(f"My seat: {s+1}")