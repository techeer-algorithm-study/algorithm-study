# 오일러 피 함수 : n 이하의 자연수 중 n과 서로소인 수의 개수를 구하는 함수

import math

n = int(input())
result = n

for i in range(2, int(math.sqrt(n)) + 1):
    if n % i == 0:  # 소인수라면
        while n % i == 0:
            n = n // i  # 현재 소인수 제거
        result = result - (result / i)  # 결괏값 갱신
if n > 1:  # n이 마지막 소인수인 경우
    result = result - (result / n)
print(int(result))
