import pprint
from random import randint

a, b = 10, 10
matrix = [[randint(0, 9) for i in range(a)]for j in range(b)]

pp = pprint.PrettyPrinter(width=len(str(matrix)) - 1)
pp.pprint(matrix)

i = 0
j = 0
i1 = -10
j1 = -1
temp = []
temp1 = []
for _ in range(len(matrix)):
    temp.append(matrix[i][j])
    i += 1
    j += 1
for _ in range(len(matrix)):
    temp1.append(matrix[i1][j1])
    i1 += 1
    j1 += -1
i = 0
j = 0
i1 = -10
j1 = -1
temp.reverse()
temp1.reverse()
for _ in range(len(matrix)):
    matrix[i][j] = temp[i]
    i += 1
    j += 1
for i in range(len(matrix)):
    matrix[i1][j1] = temp1[i]
    i1 += 1
    j1 += -1
pp = pprint.PrettyPrinter(width=len(str(matrix)) - 1)
pp.pprint(matrix)
