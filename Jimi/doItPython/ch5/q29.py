
n = int(input())
a = list(map(int, input().split()))
m = int(input())
target_list = list(map(int, input().split()))
a.sort()

for i in range(m):
    find = False
    target = target_list[i]
    start = 0
    end = len(a) - 1
    while start <= end:
        mid_i = int((start + end) / 2) 
        mid_v = a[mid_i]
        if mid_v > target:
            end = mid_i - 1 
        elif mid_v < target:
            start = mid_i + 1
        else: 
            find = True
            break
    if find:
        print(1)
    else:
        print(0)

