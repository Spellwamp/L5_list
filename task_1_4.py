import pprint
from random import randint

a, b = int(input()), int(input())
matrix = [[randint(0, 20) for i in range(a)]for j in range(b)]
matrix1 = [[randint(0, 20) for i1 in range(a)]for j2 in range(b)]
matrix_finaly = []

for i in range(len(matrix)):
    temp = []
    for j in range(len(matrix)):
        if matrix[i][j] >= matrix1[i][j]:
            temp.append(matrix[i][j])
        else: temp.append(matrix1[i][j])
    matrix_finaly.append(temp)

pp = pprint.PrettyPrinter(width=len(str(matrix)) - 1)
pp.pprint(matrix_finaly)



# import pprint
# from random import randint

# a, b = int(input()), int(input())
# matrix = [[randint(0, 20) for i in range(a)]for j in range(b)]
# matrix1 = [[randint(0, 20) for i in range(a)]for j in range(b)]
# matrix_finaly = []

# for i in range(len(matrix)):
#     temp = []
#     for j in range(len(matrix)):
#         if matrix[i][j] >= matrix1[i][j]:
#             temp.append(matrix[i][j])
#         else: temp.append(matrix1[i][j])
#     matrix_finaly.append(temp)

# pp = pprint.PrettyPrinter(width=len(str(matrix)) - 1)
# pp.pprint(matrix)
# pp.pprint(matrix1)
# pp.pprint(matrix_finaly)
