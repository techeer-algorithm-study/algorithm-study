import sys
input = sys.stdin.readline
N = int(input())
tree = {} # 트리 딕셔너리로 사용, 간단하게 관계로 표현하기 위함

for _ in range(N) :
    root, left, right = input().split() # root, right, left 데이터 받기
    tree[root] = [left, right] # 트리 딕셔너리에 데이터 저장

def preOrder(now) : # 중간-왼쪽-오른쪽 전위 순회
    if now == '.' :
        return # 자식 노드가 없으면 return
    print(now, end = '') # 현재 노드 출력
    preOrder(tree[now][0]) # 왼쪽 자식 노드 탐색
    preOrder(tree[now][1]) # 오른쪽 자식 노드 탐색

def inOrder(now): # 왼쪽-중간-오른쪽 중위 순회
    if now == '.' :
        return # 자식 노드가 없으면 return
    inOrder(tree[now][0]) # 왼쪽 자식 노드 탐색
    print(now, end='') # 현재 노드 출력
    inOrder(tree[now][1]) # 오른쪽 자식 노드 탐색

def postOrder(now) : # 왼쪽-오른쪽-중간 중위 순회
    if now == '.' :
        return # 자식 노드가 없으면 return
    postOrder(tree[now][0]) # 왼쪽 자식 노드 탐색
    postOrder(tree[now][1]) # 오른쪽 자식 노드 탐색
    print(now, end = '') # 현재 노드 출력

#preOrder - inOrder - postOrder 순으로 실행, 결과 출력
preOrder('A')
print()
inOrder('A')
print()
postOrder('A')
