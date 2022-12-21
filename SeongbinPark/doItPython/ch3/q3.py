import sys

input = sys.stdin.readline

n, m = map(int, input().split())
ary = list(map(int, input().split()))
prefix_sum = [0]  # init prefix_sum

temp = 0
for i in ary:
    temp += i
    prefix_sum.append(temp)

for i in range(m):
    a, b = map(int, input().split())
    print(prefix_sum[b] - prefix_sum[a - 1])
