import sys

input = sys.stdin.readline # 입력 받는 시간 줄이기 

num_leng, sum_leng =  map(int, input().split())
nums = list(map(int, input().split()))
sum = 0
sum_arr = [0] # 0번 인덱스를 0으로 초기화

for num in nums:
    sum += num
    sum_arr.append(sum)

for i in range(sum_leng):
    start, end = map(int, input().split())
    print(sum_arr[end] - sum_arr[start-1])

# ---------- 시간 초과 ------------

# num_leng, sum_leng =  map(int, input().split())
# nums = list(map(int, input().split()))
# result = []

# for i in range(sum_leng):
#     start, end = map(int, input().split())
#     sum = 0
#     for j in range(start - 1, end):
#         sum += nums[j]
#     result.append(sum)

# for i in result:
#     print(i)