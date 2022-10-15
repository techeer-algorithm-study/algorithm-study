n = int(input())
nums = input()
nums_list1 = nums.split(" ")
nums_list2 = [int(i) for i in nums_list1]
max_num = max(nums_list2)
avg = sum(nums_list2)/n
new_avg = avg*100/max_num
print(new_avg)