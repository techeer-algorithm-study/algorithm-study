n = int(input())
lst = [0] * 100001

for i in range(n):
    num = int(input())
    lst[num] += 1

for j in range(len(lst)):
    if lst[j] > 0:
        for k in range(lst[j]):
            print(j)