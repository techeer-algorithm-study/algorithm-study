n1 = int(input())
n2 = int(input())
temp = input().split(" ")
nums = [int(i) for i in temp]

# long way
count = 0
for i in range(0,n1):
    for j in range(i+1,n1):
        if nums[i] + nums[j] == n2:
            count += 1
print(count)

# short way
count = 0
nums = sorted(nums)
for i in range(n1):
    a = nums[i]
    b = nums[n1-1]
    if a+b == n2:
        count += 1
        n1 -= 1
    if i == n1 - 1:
        break
print(count)