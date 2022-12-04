#유클리드 호제법을 이용한 문제 풀이
#Ax + By = C 를 구하는 문제 --> 유클리드 호제법

# Ax + By = C 에서 
# C의 값이 A와 B의 최대 공약수의 배수 형태라면, --> C의 값을 최대 공약수로 변경 후 유클리드 호제법 수행
# 여기서 몫과 나머지를 이용하여 거꾸로 연산하면서 x = y', y = x' - y' * q를 계산
# (')표시는 전의 값
# 최종 x, y 값은 Ax + By = gcd(a,b) 값을 만족하게 됨
# gcd(a,b) = C 라고 가정하면 방정식의 해는 Cx,Cy 값으로 표현됨
# 이를 통해 문제를 풀어보자.

a, b, c = map(int, input().split())

def gcd(a, b):                  #최대공약수 함수 선언
    if b == 0:                  #b가 0이면 a가 최대공약수  
        return a                    
    else:
        return gcd(b, a % b)    #else 재귀함수로 최대공약수 구하기 a % b

def Excute(a, b):               
    ret = [0] * 2               #x , y 선언
    if b == 0:                  # 만약 B값이 0이면 
        ret[0] = 1              # x 를 1    
        ret[1] = 0              # y 를 0 으로 설정 후 리턴
        return ret              
    q = a // b                  # q는 a를 b로 나눈 몫
    v = Excute(b, a % b)        # 재귀 형태로 유클리드 호제법 실행

    ret[0] = v[1]               # 역순으로 올라오면서 x, y를 계산하는 로직
    ret[1] = v[0] - v[1] * q    
    return ret

mgcd = gcd(a, b)                # 최대 공약수 = gcd(a, b)

if c % mgcd != 0:               # 만약 C가 최대 공약수의 배수가 아니면 -1 출력
    print(-1)               
else:                               
    mok = int(c / mgcd)             # C/최대공약수의 값
    ret = Excute(a, b)              # 나머지가 0이 될 때까지 재귀함수를 호출하는 Excute 함수 호출
    print(ret[0] * mok , end = '')  # 결과값에 C/최대공약수의 값 곱한 결과 값 출력
    print(ret[1] * mok)             # 결과값에 C/최대공약수의 값 곱한 결과 값 출력

