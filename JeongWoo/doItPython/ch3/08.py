N = int(input())
A = list(map(int,input().split()))
A.sort()
count = 0

for x in range(N) :
    find = A[x]
    i = 0
    j = N-1
    while i < j :
        if A[i] + A[j] == find :
            if i != x and j != x :
                count += 1
                break
        elif i == x :
            i += 1
        elif j == x :
            j -= 1
        elif A[i] + A[j] < find :
            i += 1
        else :
            j -= 1

print(count)