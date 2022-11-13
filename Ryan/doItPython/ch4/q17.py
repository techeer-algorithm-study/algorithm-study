lst = list(input())
nums = [int(i) for i in lst]
newLst = []

while len(nums) > 0:
    maxNum = max(nums)
    newLst.append(maxNum)
    nums.remove(maxNum)
for j in newLst:
    print(j, end="")