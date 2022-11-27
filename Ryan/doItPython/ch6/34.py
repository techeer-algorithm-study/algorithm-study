n = int(input()) #수의 개수

ones = [] #1
zeros = [] #0
positives = [] #양수
negatives = [] #음수
total_sum = 0 #최종값

for i in range(n):
    num = int(input())
    if num < 0:
        negatives.append(num) #음수 저장
    elif num == 0:
        zeros.append(num) #0 저장
    elif num == 1:
        ones.append(num) #1 저장
    else:
        positives.append(num) #양수 저장

#절대값이 큰수 부터 작은수로 정렬
negatives.sort()
positives.sort(reverse=True)

#숫자 홀수 짝수 확인
def evenodd(lst: list) -> bool:
    """Return True if is Even
    """
    length = len(lst)
    if length % 2 == 1:
        return False
    return True

#음수:
# 음수 리스트 길이가 짝수일시:
if evenodd(negatives):
    length1 = len(negatives)
# 음수 리스트 길이가 홀수일시:
else:
    length1 = len(negatives)-1
    if len(zeros) == 0:
        total_sum += negatives[-1] #만약에 0이 존재 하지 않는다면 절대값이 제일 작은 음수를 더해준다

#양수:
# 양수 리스트 길이가 짝수일시:
if evenodd(positives):
    length2 = len(positives)
# 양수 리스트 길이가 홀수일시:
else:
    length2 = len(positives)-1
    total_sum += positives[-1] #제일 작은 양수를 합에 더해준다


for i in range(0,length1,2):
    a = negatives[i]
    b = negatives[i+1]
    total_sum += (a*b) #묶은 숫자 더하기

for j in range(0,length2,2):
    c = positives[j]
    d = positives[j+1]
    total_sum += (c*d) #묶은 숫자 더하기

total_sum += sum(ones) #1들 합에 더하기

print(total_sum)