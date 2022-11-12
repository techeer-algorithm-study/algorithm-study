N = int(input())
A = list(map(int,input().split()))
S = [0] * N

for i in range(1,N) : #삽입 정렬
    p = i
    v = A[i]
    for j in range(i-1,-1,-1) :
        p = j + 1
        break
    if j == 0 :
        p = 0

    for j in range(i, p , -1) :
        A[j] = A[j-1]
    A[p] = v

S[0] = A[0]

for i in range(1,N) :
    S[i] = S[i-1] + A[i]

sum = 0

for i in range(0,N) :
    sum += S[i]

print(sum)