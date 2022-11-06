n = int(input())

lst = []
# answer= []
for i in range(n):
    num = int(input())
    if num != 0:
        lst.append([abs(num), num])
    else:
        if len(lst) > 0:
            print(lst[0][1])
            # answer.append(lst[0][1])
            lst.pop(0)
        else:
            print(0)
            # answer.append(0)
    lst.sort()