from collections import deque

n = int(input())

lst = []
nodes = []
distance = [0] * (n+1)
visit = [False] * (n+1)

for i in range(n):
    line = input().split(" ")
    int_line = [int(i) for i in line]
    lst.append(int_line[:-1])
nodes.append([])
for j in lst:
    temp = []
    if len(j) > 3:
        for l in range(1,len(j)-1,2):
            key2 = j[l]
            dis = j[l+1]
            temp.append((key2, dis))
    else:
        temp.append((j[1],j[2]))
    nodes.append(temp)


def bfs_distance(node):
    queue = deque()
    queue.append(node)
    visit[node] = True
    while len(queue) > 0:
        val = queue.popleft()
        for i in nodes[val]:
            if visit[i[0]] == False:
                queue.append(i[0])
                distance[i[0]] = distance[val] + i[1]
                visit[i[0]] = True
                bfs_distance(val)
                
bfs_distance(1)
maxNum = 1
for j in range(2,n+1):
    if distance[maxNum] < distance[j]:
        maxNum = j
distance = [0] * (n+1)
visit = [False] * (n+1)
bfs_distance(maxNum)
for i in range(len(nodes)):
    print(f"Node {i} : {nodes[i]}")
print(max(distance))

# 5
# 1 3 2 -1
# 2 4 4 -1
# 4 1 2 4 3 -1
# 4 2 4 3 3 5 6 -1
# 5 4 6 -1