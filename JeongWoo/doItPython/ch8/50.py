import sys
input = sys.stdin.readline
sys.setrecursionlimit(1000000)
N, M = map(int, input().split())
parent = [0] * (N+1) # 대표 노드 저장 리스트

def find(a) : 
    if a == parent[a] : # a가 대표 노드면 리턴
        return a 
    else : # a의 대표 노드값을 find(parent[a])값으로 저장 -> 재귀 함수 형태
        parent[a] = find(parent[a])
        return parent[a]

def union(a,b) :
    a = find(a) # a와 b의 대표 노드 찾기
    b = find(b)
    if a != b : # 두 원소의 대표 노드끼리 연걸
        parent[b] = a

def checkSame(a,b) : # 두 원소 같은 집합 확인
    a = find(a)
    b = find(b)
    if a == b : # 두 대표 노드 같으면 true
        return True
    return False

for i in range(0, N+1) :
    parent[i] = i # 대표 노드를 자기 자신으로 초기화

for i in range(M) :
    question, a, b = map(int, input().split())
    if question == 0 : # 질문이 0이면
        union(a, b) # 집합 합치기 (union 연산)
    else :
        if checkSame(a, b) : # 같은 집합 원소인지 확인하고 결과값 출력
            print("YES")
        else:
            print("NO")