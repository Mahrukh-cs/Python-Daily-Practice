# sum of matrix
matrix =  [[0, 1, 2], [3, 4, 5], [7, 8, 9]]

total = 0

for i in range(0, 3):
    for j in range(0, 3):
        total = total + matrix[i][j]

print(f"Total of matrix = {total}")