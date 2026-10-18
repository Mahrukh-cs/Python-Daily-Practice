"""
given a 4x4 matrix, print only the border elements and replace the inner elements with an asterisk(*).
# border condition: element is on the first row, last row, first column, or last column
# inner elements: row index is not 0 or 3, AND column index is not 0 or 3
Given 
1  2  3  4
5  6  7  8
9  10 11 12
13 14 15 16
Output
1  2  3  4
5  6  7  8
9  10 11 12
13 14 15 16
"""
matrix = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]
rows = len(matrix)
columns = len(matrix[0])
for i in range(0, rows):
    for j in range(0, columns):
        # if (i==1 and j==1) or (i==1 and j==2) or (i==2 and j==1) or (i==2 and j==2):
        if (i == 0 or j == 0 or i == 3 or j == 3)  :
            print(matrix[i][j], end=" ")
        else:
            print("*", end=" ")
    print()