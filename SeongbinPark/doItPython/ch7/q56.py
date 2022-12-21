import sys 
input = sys.stdin.readline
from queue import PriorityQueue

V,E=map(int, input().split) # 노드 개수 V, 에지 개수 E
K=int(input()) # 출발 노드
distance = [sys.maxsize]*(V+1) # 무한으로 초기화
visited=[False]*(V+1) # 방문한 노드인지
myList=[[] for _ in range(V+1)] # 에지 저장
q=PriorityQueue()

for _ in range(E):
    u,v,w=map(int, input().split()) # 출발, 도착, 비용
    myList[u].append((v,w))

q.put((0,K)) # 출발 노드 넣기
distance[K]=0 # 출발노드는 거리가 0

while q.qsize()>0: # 큐가 빌 때 까지
    current=q.get() # 노드 가져오기
    c_v=current[1]
    if visited[c_v]: # 이미 방문한 노드면 처음부터
        continue
    visited[c_v]=True # 방문한 노드로 변경
    for tmp in myList[c_v]:
        next=tmp[0]
        value=tmp[1]
        if distance[next]>distance[c_v]+value: # 새 비용이 더 적으면
            distance[next]=distance[c_v]+value # 그 비용으로 해당 노드 갱신
            q.put((distance[next], next)) # 큐도 갱신

for i in range(1,V+1):
    if visited[i]: # 방문 가능한 노드
        print(distance[i])
    else: # 방문 불가능한 노드
        print("INF")
