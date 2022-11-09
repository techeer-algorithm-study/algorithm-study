n = int(input())

lst = []

for i in range(n):
    num = int(input())
    lst.append(num)

for j in range(n):
    for k in range(j,n):
        if lst[j] > lst[k]:
            a = lst[j]
            b = lst[k]
            lst[j] = b
            lst[k] = a
for l in lst:
    print(l)