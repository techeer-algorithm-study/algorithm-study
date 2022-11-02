leng = int(input())
scores = list(map(int, input().split())) # 입력값을 공백 기준으로 분리 후 각 원소를 정수로 형변환

max = max(scores)
sum = 0

for i in range(leng):
    scores[i] = scores[i] / max * 100 
    sum += scores[i]

new_avg = sum / leng
print(new_avg)
