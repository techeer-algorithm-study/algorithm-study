n = int(input())
lst = input().split(" ")
nums = [int(i) for i in lst]
newLst = []

while len(nums) > 0:
    minNum = min(nums)
    newLst.append(minNum)
    nums.remove(minNum)
sumNums = [0]*n
sumNums[0] = newLst[0]

for j in range(len(newLst)):
    sumNums[j] = sumNums[j-1] + newLst[j]

print(sum(sumNums))