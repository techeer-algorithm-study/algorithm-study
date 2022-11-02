a, b = input().split(" ")
a = int(a)
b = int(b)
lst = []
for i in range(a):
    row = input().split(" ")
    lst.append(row)
for j in range(b):
    total = 0
    startx, starty, endx, endy = input().split(" ")  
    startx = int(startx) - 1
    starty = int(starty) - 1
    endx = int(endx)
    endy = int(endy)
    for k in range(startx,endx):
        for l in range(starty,endy):
            y = lst[k][l]
            total += int(y)
    print(total)