n = int(input())
count = 0
lst= []
for i in range(1,n+1):
    lst.append(i)
for j in range(0,n+1):
    for k in range(j,n+1):
        sumNum = sum(lst[j:k])
        if sumNum == n:
            count += 1
print(count)