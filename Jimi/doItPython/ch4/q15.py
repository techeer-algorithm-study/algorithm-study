n = int(input())
arr = [0] * n

for i in range(n):
    arr[i] = int(input())

for i in range(n):
    for j in range(i):
        if(arr[j] > arr[i]):
            tmp = arr[i]
            arr[i] = arr[j]
            arr[j] = tmp

for i in range(n):
    print(arr[i])
