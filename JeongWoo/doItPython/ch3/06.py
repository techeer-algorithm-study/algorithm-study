n = int(input())
count = 0
getsum = 0
for x in range(1,n+1) :
    getsum = 0
    for y in range(x, n+1) :
        getsum += y
        if getsum == n:
            count += 1

print(count)
