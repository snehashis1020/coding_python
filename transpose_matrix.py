def transpose_matrix(matrix):
    rows = len(matrix)
    cols = len(matrix[0])
    transpose = []
    for i in range(cols):
        new_row = []
        for j in range(rows):
            new_row.append(matrix[j][i])
        transpose.append(new_row)
    return transpose
rows = int(input("Enter number of rows: "))
cols = int(input("Enter number of columns: "))
matrix = []
print("Enter matrix elements row-wise:")
for i in range(rows):
    row = list(map(int, input().split()))
    matrix.append(row)
result = transpose_matrix(matrix)
print("Transpose matrix:")
for row in result:
    print(row)
