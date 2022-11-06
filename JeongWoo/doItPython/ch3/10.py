from collections import deque
N, L = map(int, input().split())
x = deque()
now = list(map(int, input().split()))

for i in range(N) :
    while x and x[-1][0] > now[i]:
        x.pop()
    x.append((now[i],i))
    if x[0][1] <= i - L :
        x.popleft()
    print(x[0][0], end='')