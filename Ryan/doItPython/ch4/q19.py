n, m = input().split(" ")
n = int(n)
m = int(m)
lst = input().split(" ")

newLst = []
additional = []
nums = [int(i) for i in lst]

mid = n//2

pivot = nums[mid]

nums.remove(pivot)

for i in range(n-2,-1,-1):
    if nums[i] < pivot:
        newLst.append(nums[i])
    else:
        additional.append(nums[i])
additional.reverse()
newLst.append(pivot)
result = newLst + additional
print(result[m-1])