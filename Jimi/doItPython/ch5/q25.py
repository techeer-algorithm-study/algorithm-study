import sys 
input = sys.stdin.readline
n, m = map(int, input().split())

arrive = False # 도착 확인 변수 
visited = [False] * (n + 1) # 방문 기록 리스트 
A = [[] for _ in range(n+1)] # 그래프 데이터 인접 리스트 

def DFS(now, depth):
    global arrive # 전역변수 사용 
    if depth == 5: # 깊이가 5가 되면 함수 종료 
        arrive = True
        return 
    visited[now] = True # 방문 여부 변경 
    for i in A[now]:
        if not visited[i]: # 방문하지 않은 곳 방문
            DFS(i, depth + 1) # 재귀 호출 마다 값 증가 


for _ in range(m): # 인접 리스트에 그래프 데이터 저장
    s, e = map(int, input().split())
    A[s].append(e)
    A[e].append(s)

for i in range(n): # 노드마다 DFS 실행
    DFS(i, 1)
    if arrive: # 5에 도달하면 반복문 종료 
        break

if arrive: # 5에 도달하면 1 출력
    print(1)
else:
    print(0)




