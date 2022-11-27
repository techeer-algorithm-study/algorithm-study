n = int(input()) # total number of inputs

nums = input().split(" ") # number inputs
lst1 = [int(i) for i in nums] # number inputs converted to integers

count = 0 # count for swaps happened
def sort_list(lst): #function for sorting
    """This function is for sorting a list from small to large
    """
    global count
    n = len(lst)
    for j in range(n):
        for k in range(j,n):
            if lst[j] > lst[k]:
                a = lst[j]
                b = lst[k]
                lst[j] = b
                lst[k] = a
                count += 1
    return lst


lst2 = [] # lst2 is a lst starting with 2 components
for j in range(0,n,2):
    lst2.append(lst1[j:j+2]) #creates a list with only 2 components of the list

i = len(lst2) - 1
while len(lst2) > 1:
    print(lst2)
    lst2[i] = sort_list(lst2[i]) # sort the list[i] inside list
    lst2[i-1] = sort_list(lst2[i-1]) # sort list left of the list[i]
    if lst2[i][0] > lst2[i-1][0]: # check index values and concatenate accordingly. This parts needs revision
        lst2[i-1] += lst2[i]
        lst2.remove(lst2[i])
    else:
        lst2[i] += lst2[i-1]
        lst2.remove(lst2[i-1])
    i -= 2
result = sort_list(lst2[0]) # sort the final list once again
print(result) #print the resulting list
print(count) #print the number of swaps happened