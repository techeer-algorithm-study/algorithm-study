n = int(input())

lst1 = []
for i in range(n):
    num = int(input())
    lst1.append(num)

def sort_list(lst):
    n = len(lst)
    for j in range(n):
        for k in range(j,n):
            if lst[j] > lst[k]:
                a = lst[j]
                b = lst[k]
                lst[j] = b
                lst[k] = a
    return lst
lst2 = []
for j in range(0,n,2):
    lst2.append(lst1[j:j+2])

i = len(lst2) - 1
while len(lst2) > 1:
    lst2[i] = sort_list(lst2[i])
    lst2[i-1] = sort_list(lst2[i-1])
    if lst2[i][0] > lst2[i-1][0]:
        lst2[i-1] += lst2[i]
        lst2.remove(lst2[i])
    else:
        lst2[i] += lst2[i-1]
        lst2.remove(lst2[i-1])
    i -= 2
result = lst2[0]
print(result)