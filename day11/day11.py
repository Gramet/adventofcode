from copy import deepcopy

with open('input', 'r') as f:
   lines = f.readlines()

dict_seat = {'.': -1, 'L': 0, '#': 1}

def change_seats(mat):
   mat_cop = deepcopy(mat)
   for row in range(1, len(mat)-1):
      for col in range(1, len(mat[row])-1):
         num_neigh = 0
         num_neigh += 0 if mat_cop[row-1][col-1] == -1 else mat_cop[row-1][col-1]
         num_neigh += 0 if mat_cop[row-1][col] == -1 else mat_cop[row-1][col]
         num_neigh += 0 if mat_cop[row-1][col+1] == -1 else mat_cop[row-1][col+1]
         num_neigh += 0 if mat_cop[row][col-1] == -1 else mat_cop[row][col-1]
         num_neigh += 0 if mat_cop[row][col+1] == -1 else mat_cop[row][col+1]
         num_neigh += 0 if mat_cop[row+1][col-1] == -1 else mat_cop[row+1][col-1]
         num_neigh += 0 if mat_cop[row+1][col] == -1 else mat_cop[row+1][col]
         num_neigh += 0 if mat_cop[row+1][col+1] == -1 else mat_cop[row+1][col+1]

         if mat_cop[row][col] == 0 and num_neigh == 0:
            mat[row][col] = 1
         elif mat_cop[row][col] == 1 and num_neigh >= 4:
            mat[row][col] = 0
   
   return mat

def find_nearest(mat, row, col, dir_row, dir_col):
   dir_row_ori = dir_row
   dir_col_ori = dir_col
   while True:
      if row+ dir_row == len(mat) or row + dir_row == -1 or col + dir_col == len(mat[row]) or col+dir_col == -1:
         return 0
      if mat[row + dir_row][col + dir_col] == -1:
         dir_row += dir_row_ori
         dir_col += dir_col_ori
      else:
         return mat[row + dir_row][col + dir_col]

def change_seats_far(mat):
   mat_cop = deepcopy(mat)
   for row in range(1, len(mat)-1):
      for col in range(1, len(mat[row])-1):
         num_neigh = 0
         num_neigh += find_nearest(mat_cop, row, col, -1, -1)
         num_neigh += find_nearest(mat_cop, row, col, -1, 0)
         num_neigh += find_nearest(mat_cop, row, col, -1, 1)
         num_neigh += find_nearest(mat_cop, row, col, 0, -1)
         num_neigh += find_nearest(mat_cop, row, col, 0, 1)
         num_neigh += find_nearest(mat_cop, row, col, 1, -1)
         num_neigh += find_nearest(mat_cop, row, col, 1, 0)
         num_neigh += find_nearest(mat_cop, row, col, 1, 1)

         if mat_cop[row][col] == 0 and num_neigh == 0:
            mat[row][col] = 1
         elif mat_cop[row][col] == 1 and num_neigh >= 5:
            mat[row][col] = 0
   
   return mat

         
mat = [[-1] * (len(lines[0].strip('\n'))+2)]
for line in lines:
   mat.append([-1] + [dict_seat[x] for x in line.strip('\n')] + [-1])
mat.append([-1] * (len(lines[0].strip('\n'))+2))

num_floor = -sum(sum(row) for row in mat)


for cnt in range(1000):
   if mat == change_seats(deepcopy(mat)):
      break
   else:
      mat = change_seats(deepcopy(mat))
   
print(mat)

print(cnt)
num_occ = sum(sum(row) for row in mat) + num_floor
print(num_occ)

# Part 2 
mat = [[-1] * (len(lines[0].strip('\n'))+2)]
for line in lines:
   mat.append([-1] + [dict_seat[x] for x in line.strip('\n')] + [-1])
mat.append([-1] * (len(lines[0].strip('\n'))+2))

for cnt in range(1000):
   if mat == change_seats_far(deepcopy(mat)):
      break
   else:
      mat = change_seats_far(deepcopy(mat))

print(cnt)
num_occ = sum(sum(row) for row in mat) + num_floor
print(num_occ)