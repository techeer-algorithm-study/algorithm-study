n, m = input().split()
n = int(n)#4
m = int(m)#2

dna = list(input().lower())#gata
temp = list(input().split())#ignore

acgt_lst = [int(i) for i in temp]#[1,0,0,1]

count = 0

# dna_counts = [dna.count(i) for i in lst] #[2,0,1,1]

#check if valid num of acgt
iter_len = n - m + 1

for j in range(iter_len):
    window = dna[j:j+m]
    a = window.count("a")
    c = window.count("c")
    g = window.count("g")
    t = window.count("t")
    if a >= acgt_lst[0] and c >= acgt_lst[1] and g >= acgt_lst[2] and t >= acgt_lst[3]:
        count += 1


print(count)