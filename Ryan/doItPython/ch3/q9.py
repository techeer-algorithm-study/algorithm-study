from itertools import combinations

n, m = input().split()
n = int(n)#4
m = int(m)#2

dna = list(input().lower())#gata
temp = list(input().split())#ignore

acgt_lst = [int(i) for i in temp]#[1,0,0,1]

lst = ["a","c","g","t"]
count = 0
flag = True

dna_counts = [dna.count(i) for i in lst] #[2,0,1,1]

#check if valid num of acgt
for i in range(len(dna_counts)):
    diff = dna_counts[i] - acgt_lst[i]
    if diff < 0:
        flag = False

#if valid
if flag:
    combs = list(set(list(combinations(dna, m))))
    for i in combs:
        if i.count("a") >= acgt_lst[0] and i.count("c") >= acgt_lst[1] and i.count("g") >= acgt_lst[2] and i.count("t") >= acgt_lst[3]:
            count += 1

print(count)