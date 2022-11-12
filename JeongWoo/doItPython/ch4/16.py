import sys
input = sys.stdin.readline

n = int(input())
A = []

for i in range(n) :
    A.append(int(input()),i)

max = 0
sorted_A = sorted(A)

for i in range(n) :
    if max < sorted_A[i][1] - i :
        max = sorted_A[i][1] - i

print(max + 1)