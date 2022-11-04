n, l = input().split(" ")
n = int(n)
l = int(l)
nums = input().split(" ")
for i in range(n):
    aI = i + 1
    aL = i + 1 - l
    if aL < 0:
        aL = 0
    numList = nums[aL:aI]
    minNum = min(numList)
    print(minNum, end=" ")