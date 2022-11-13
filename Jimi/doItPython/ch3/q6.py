
num = int(input())

count = 1
sum = 1
start, end = 1, 1


while end != num:
    if sum < num:
        end += 1
        sum += end
    elif sum > num:
        sum -= start
        start += 1
    else:
        count += 1
        end += 1
        sum += end

print(count)