n = int(input())
temp = input().split(" ")
nums = [int(i) for i in temp]

count = 0
lst = []
for i in range(n):#target
    for j in range(n):#first
        for k in range(j+1,n):#second
            a = nums[i]
            b = nums[j]
            c = nums[k]
            if a == (b + c):
                if a not in lst:
                    print("b:", b, "c:", c)
                    lst.append(a)
                    count += 1
                    break
print(count)