import sys
input = sys.stdin.readline
N = int(input()) # 도시 개수
M = int(input()) # 노선 개수
distance = [[sys.maxsize for j in range(N+1)] for i in range(N+1)] # 충분히 큰 값으로 초기화

for i in range(1, N+1) :
    distance[i][i] = 0

for i in range(M) :
    s, e, v = map(int, input().split())
    if distance[s][e] > v :
        distance[s][e] = v

for k in range(1, N+1) : # 3중 for문의 순서가 중요함. k가 가장 바깥쪽
    for i in range(1, N+1) :
        if distance[i][j] > distance[i][k] + distance[k][j] :
            distance[i][j] = distance[i][k] + distance[k][j]

for i in range(1, N+1) :
    for j in range(1, N+1) :
        if distance[i][j] == sys.maxsize :
            print(0, end = ' ') # 도착할 수 없는 경로 (리스트값이 최초 초기화하기에 충분히 큰 수이면 0 출력)
        else :
            print(distance[i][j], end = ' ')
    print()