#if notn = int(input())
n = int(input())

lst = []

for i in range(n):
    num = int(input())
    lst.append(num)

for j in range(1,n):
    swapped = True
    for k in range(0,n-j):
        if lst[k] > lst[k+1]:
            swapped = False
            a = lst[k+1]
            b = lst[k]
            lst[k+1] = b
            lst[k] = a
    if swapped:
        print(j)
        break