m = int(input())
temp = input().split(" ")

n = [int(i) for i in temp]

for j in range(m-1):
    pivot = n[j]
    numList = n[j+1:]
    if max(numList) < pivot:
        print(-1, end=" ")
    else:
        for k in numList:
            if k > pivot:
                print(k, end=" ")
                break
print(-1)
