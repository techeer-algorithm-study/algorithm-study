lengths = input().split(" ")
num_list = input().split(" ")
for i in range(int(lengths[1])):
    n = input().split(" ")
    new_nums = num_list[int(n[0])-1:int(n[1])]
    sum_list = sum([int(i) for i in new_nums])
    print(sum_list)