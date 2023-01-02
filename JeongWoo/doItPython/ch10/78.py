import sys
input = sys.stdin.readline
D = [[0 for j in range(15)] for i in range(15)]

for i in range(1,15) : # 리스트 초기화
    D[i][1] = 1 # i층의 1호는 항상 1의 값을 지니기 때문에 초기화할 수 있음
    D[0][i] = i # 0층의 i호는 i의 값을 지니도록 문제에서 주어짐

for i in range(1,15) :
    for j in range(2, 15) :
        D[i][j] = D[i][j-1] + D[i-1][j] # 일반화된 점화식

T = int(input()) # 테스트 케이스

for i in range(0, T) :
    K = int(input()) # 층수 입력
    N = int(input()) # 호수 입력
    print(D[K][N])