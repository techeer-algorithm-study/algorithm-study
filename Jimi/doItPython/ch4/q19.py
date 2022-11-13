import sys
input = sys.stdin.readline
n, k = map(int, input().split())
a = list(map(int, input().split()))

def quickSort(S, E, K):
    global a
    if S < E:
        pivot = partition(S, E)
        if pivot == K:
            return
        elif K < pivot:
            quickSort(S, pivot-1, K)
        else:
            quickSort(pivot+1, E, K)

def swap(i, j):
    global a
    temp = a[i]
    a[i] = a[j]
    a[j] = temp

def partition(S, E):
    global a
    if S + 1 == E:
        if a[S] > a[E]:
            swap(S,E)
        return E
    
    M = (S + E) // 2
    swap(S, M)
    pivot = a[S]
    i = S + 1
    j = E

    while i <= j:
        while pivot < a[j] and j > 0:
            j = j - 1
        while pivot > a[i] and i < len(a) - 1:
            i = i + 1
        if i <= j:
            swap(i, j)
            i = i+1
            j = j-1
    a[S] = a[j]
    a[j] = pivot
    return j

quickSort(0, n-1, k-1)
print(a[k-1])