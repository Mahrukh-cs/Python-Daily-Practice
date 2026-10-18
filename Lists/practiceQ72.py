"""
given a 3x3 matrix, print only anti-diagonal(top-right to bottom-left) elements 
and replace everything else with an asterisk(*).
Given:
1 2 3
4 5 6
7 8 9
Output:
* * 3
* 5 *
7 * *
"""
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
rows = len(matrix)
columns = len(matrix[0])
for i in range(0, rows):
    for j in range(0, columns):
        # if (i==0 and j==2) or (i==1 and j==1) or (i==2 and j==0):
        if i+j == (rows-1):
            print(matrix[i][j], end=" ")
        else:
            print("*", end=" ")
    print()
