

arr = list(input())

for i in range(len(arr)):
    max = i
    for j in range(i+1, len(arr)):
        if arr[j] > arr[max]:
            max = j
    if arr[i] < arr[max]:
        tmp = arr[i]
        arr[i] = arr[max]
        arr[max] = tmp

for i in range(len(arr)):
    print(arr[i])