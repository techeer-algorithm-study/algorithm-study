N = int(input())
A = [[] for _ in range(N)] # 인접 리스트
visited = [False] * (N) # DFS 탐색 여부 저장 리스트
D = [0] * (N) # 각 노드값 저장 리스트
lcm = 1 # 최소 공배수 

def gcd(a, b): # 최대공약수 구하는 함수 
    if b == 0:
        return a
    else:
        return gcd(b, a % b)

def DFS(v): # 탐색 함수 
    visited[v] = True
    for i in A[v]: # 
        next = i[0]
        if not visited[next]:
            D[next] = D[v] * i[2] // i[1] # 다음 노드의 값 = 현재 노드의 값 * 비율 
            DFS(next)

for i in range(N - 1): # 입력 받기 
    a, b, p, q = map(int, input().split()) 
    A[a].append((b, p, q)) # 인접 리스트에 다 저장
    A[b].append((a, q, p))
    lcm *= (p * q // gcd(p, q)) # 최소공배수 구하기: 두 수의 곱을 최대 공약수로 나눈 것 

D[0] = lcm # 0번 노드에 최소 공배수 저장 
DFS(0) # 0번에서 탐색 시작 
mgcd = D[0] 
for i in range(1, N):
    mgcd = gcd(mgcd, D[i]) # DFS 수행 후 업데이트된 D 값들의 최대공약수 계산 
for i in range(N):
    print(int(D[i] // mgcd), end=' ') # 각 노드의 값을 최대 공약수로 나누어 출력 