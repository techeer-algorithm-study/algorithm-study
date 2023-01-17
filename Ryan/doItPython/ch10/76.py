def factorial(num):
    if num == 1:
        return num
    return num * factorial(num-1)

n, k = input().split(" ")
n = int(n)
k = int(k)

#combination formula
comb = int(factorial(n)/(factorial(n-k)*factorial(k)))
print(comb)

#combination tree
tree = [[0 for i in range(n+1)] for j in range(n+1)]
for c in range(n+1):
    tree[c][1] = c
    tree[c][0] = 1
    tree[c][c] = 1

for i in range(3,n+1):
    for j in range(2,i):
        tree[i][j] = tree[i-1][j] + tree[i-1][j-1]

print(tree[n][k])
for i in tree:
    print(i)
