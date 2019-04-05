import pprint

matrix = [[int(x) for x in input().split()[:4]]for i in range(4)]
row_sum = list(map(sum, matrix))
for i in range(len(matrix)):
    matrix[i].append(row_sum[i])

pp = pprint.PrettyPrinter(width=56)
pp.pprint(matrix)
