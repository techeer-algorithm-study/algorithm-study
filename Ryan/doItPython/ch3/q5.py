n, m = input().split(" ")
n = int(n)
m = int(m)
nums = input().split(" ")

count = 0
num = 0
lst = nums.copy()
lst1 = [0]*m
for i in range(0,n):
    num += int(nums[i])
    mod = num % m
    lst[i] = mod
for j in lst:
    if j == 0:
        count += 1
    lst1[j] += 1
for k in lst1:
    if k > 1:
        val = (k*(k-1)//2)
        count += val
print(count)