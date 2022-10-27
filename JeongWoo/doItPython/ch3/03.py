import sys
input = sys.stdin.readline # 반복문으로 여러 줄 입력받을 때 사용
data, line = map(int, input(). split())
number = list(map(int, input().split()))
sum = [0]
temp = 0
for i in number :
    temp = temp + i
    sum.append(temp)

for i in range(line) :
    s, e = map(int, input().split())
    print(sum[e] - sum[s-1]) # 구간합을 바로 구할 수 있는 방법

# 1차원 배열의 구간합을 구하는 문제. 0번 인덱스부터 해당 칸까지의 누적 합을 구한 다음, 이를 이용하여 구간 합을 구하기.