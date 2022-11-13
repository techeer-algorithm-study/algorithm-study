from collections import deque
N = int(input())
M = deque()

for i in range(1, N+1) :
    M.append(i)

while len(M) > 1 :
    M.popleft()
    M.append(M.popleft())

print(M[0])