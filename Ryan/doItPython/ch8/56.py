# n,m = input().split(" ")
# n = int(n) #node
# m = int(m) #edge
# start_node = int(input())

# lst = [[] for i in range(n+1)]

# for i in range(m):
#     s_node, e_node, dist = input().split()
#     s_node = int(s_node)
#     e_node = int(e_node)
#     dist = int(dist)
#     lst[s_node].append([e_node, dist])

# data_lst = [[0 for i in range(n+1)] for j in range(m+1)]

# for i in range(0,n+1):
#     if i == start_node:
#         data_lst[i][start_node] = 0
#     point = lst[i] #[2,2],[3,3]
#     for j in point:
#         s = j[0]
#         v = j[1]
#         data_lst[i][s] = v
#     for k in range(len(data_lst[-1])):
#         data_lst[-1][k] += data_lst[i][k]
# for i in data_lst:
#     print(i)
import sys
from queue import PriorityQueue

V, E = map(int,input().split())

K = int(input()) #initial start
dist = [sys.maxsize] * (V+1) #distance list with max number
visited = [False] * (V+1) #boolean of visited or not
myList = [[] for i in range(V+1)] #list of (node,val)
q = PriorityQueue()


for i in range(E):
    u,v,w = map(int,input().split())
    myList[u].append((v,w)) #2d list of (node,val) where the index of list is the start node

q.put((0,K)) #start node
dist[K] = 0 #node of start is 0

while q.qsize() > 0:
    current = q.get() #tuple from queue
    current_val = current[1] #the end node
    if visited[current_val]: #check if the node was visited
        continue
    visited[current_val] = True
    for temp in myList[current_val]:
        print("target node and val:", temp)
        next_val = temp[0]
        val = temp[1]
        print("current distance list:", dist)
        if dist[next_val] > dist[current_val] + val:
            dist[next_val] = dist[current_val] + val
            q.put((dist[next_val], next_val))
        print("num(s) in queue:", q.queue)
for i in range(1, V+1):
    if visited[i]:
        print(dist[i]) #if visited
    else:
        print("INF") #if not visited