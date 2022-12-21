import sys
from collections import deque
input = sys.stdin.readline

N, M, K, X = map(int, input().split()) # 노드개수, 에지개수, 목표거리, 시작점
A = [[] for _ in range(N+1)] # 그래프 데이터 저장 인접 리스트
answer = [] # 정답 리스트
visited = [-1] * (N+1) # 방문 거리 저장 리스트

def BFS(v) : # BFS 탐색을 최단 거리값을 리스트에 저장
    queue = deque()
    queue.append(v)
    visited[v] += 1 # 거리 저장형태로 1 증가
    while queue : # 큐가 비어있을때
        now_Node = queue.popleft() # 큐에서 노드 데이터 가져오기
        for i in A[now_Node] : 
            if visited[i] == -1 : # 노드에 연결되어 있지만 방문하지 않은 노드
                visited[i] = visited[now_Node] + 1 # visited 리스트값 1 증가
                queue.append(i) # 큐에 노드 삽입

for _ in range(M) : 
    S, E = map(int, input().split())
    A[S].append(E) # A 인접 리스트에 그래프 데이터 저장

BFS(X)

for i in range(N + 1) :
    if visited[i] == K : # 방문 거리가 K인 노드의 숫자를 정답 리스트에 더하기
        answer.append(i)

if not answer :
    print(-1)
else :
    answer.sort()
    for i in answer :
        print(i) # 정답 리스트 정렬하고 출력