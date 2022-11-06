from queue import PriorityQueue
import sys
print = sys.stdout.write
input = sys.stdin.readline
N = int(input())
M = PriorityQueue()

for i in range(N) :
    request = int(input())
    if request == 0 :
        if M.empty() :
            print('0\n')
        else :
            temp = M.get()
            print(str((temp[1]))+'\n')
    else :
        M.put((abs(request), request))