matrix = [[i + (j * 10) for i in range(10)]for j in range(100)]
res = len([i for i in matrix for j in i if j in range(10, 100)])
