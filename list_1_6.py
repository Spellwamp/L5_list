import pprint
from random import randint

a, b = 3, 3
matrix = [[randint(0, 9) for i in range(a)]for j in range(b)]

matrix = [list(i) for i in zip(*matrix)]
matrix.sort()
matrix = [list(i) for i in zip(*matrix)]

pp = pprint.PrettyPrinter(width=len(str(matrix)) - 1)
pp.pprint(matrix)
