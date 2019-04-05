from random import randint
a, b = int(input()), int(input())
matrix = [[randint(0, 20) for i in range(a)]for j in range(b)]

# col
matrix.append([])
for i in range(len(matrix[0])):
    temp = 0
    for j in range(len(matrix) - 1):
        temp += matrix[j][i]
    matrix[len(matrix) - 1].append(sum1)

# row
row_sum = list(map(sum, matrix))
for i in range(len(matrix) - 1):
    matrix[i].append(row_sum[i])
