"""
given a 3x3 matrix as input, print its lower triangle.
Replace all elements in lower triangle (below the main diagonal) with an asterisk(*).
Given
1 2 3
4 5 6
7 8 9
Output
1 2 3
* 5 6
* * 9
"""
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
rows = len(matrix)
columns = len(matrix[0])
for i in range(0, rows):
    for j in range(0, columns):
        if i>j:
            print("*", end=" ")
        else:
            print(matrix[i][j], end=" ")
    print()
