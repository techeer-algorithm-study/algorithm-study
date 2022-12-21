import sys

input = sys.stdin.readline
INF = int(1e9)


v, e = map(int, input().split()) # 노드의 개수, 간선의 개수를 입력
edges = [] # 모든 간선에 대한 정보를 담는 리스트 만들기
distance = [INF] * (v + 1) # 최단 거리 테이블을 모두 무한으로 초기화

for _ in range(e): # 모든 간선의 정보 입력
    a, b, c = map(int, input().split())
    edges.append((a, b, c))


def bellman_ford(start): # 벨만 포드 알고리즘 함수
    distance[start] = 0 # 시작 노드 대해서 초기화
    # 전체 v - 1번의 라운드(round)를 반복
    for i in range(v):
        # 매 반복마다 '모든 간선'을 확인한다.
        for j in range(e):
            cur_node = edges[j][0]
            next_node = edges[j][1]
            edge_cost = edges[j][2]
            # 현재 간선을 거쳐서 다른 노드로 이동하는 거리가 더 짧은 경우
            if distance[cur_node] != INF and distance[next_node] > distance[cur_node] + edge_cost:
                distance[next_node] = distance[cur_node] + edge_cost
                # v번째 라운드에서도 값이 갱신된다면 음수 순환이 존재
                if i == v - 1:
                    return True

    return False


# 벨만 포드 알고리즘 수행
negative_cycle = bellman_ford(1)

# 음수 순환이 존재하면 -1 출력 (음수 순환
if negative_cycle:
    print("-1")
else:
    # 1번 노드를 제외한 다른 모든 노드로 가기 위한 최단 거리를 출력
    for i in range(2, v + 1):
        if distance[i] == INF: # 도달할 수 없는 경우 -1 출력
            print("-1")
        else:     # 도달할 수 있으면 거리 출력
            print(distance[i])