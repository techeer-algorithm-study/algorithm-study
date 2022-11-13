import sys

input = sys.stdin.readline

dim, sum_leng = map(int, input().split())
matrix = [[0] * (dim+1)]
d = [[0] * (dim+1) for _ in range(dim+1)]

for i in range(dim):
    row = [0] + [int(x) for x in input().split()]
    matrix.append(row)

for i in range(1, dim + 1):
    for j in range(1, dim + 1):
        d[i][j] = d[i][j-1] + d[i-1][j] - d[i-1][j-1] + matrix[i][j]

for _ in range(sum_leng):
    x1, y1, x2, y2 = map(int, input().split())
    result = d[x2][y2] - d[x1-1][y2] - d[x2][y1-1] + d[x1-1][y1-1]
    ## 이 부분 이해가 안갑니다.. 
    print(result)

