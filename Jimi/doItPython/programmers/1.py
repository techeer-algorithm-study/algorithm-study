dic = {'zero':0, 'one':1, 'two':2, 'three':3, 'four':4, 'five':5, 'six':6, 'seven':7, 'eight':8, 'nine':9}

def solution(s):
    answer = "" # 숫자 배열
    word = "" # 임시 배열
    for element in s: # 입력받은 문자열 요소 하나하나씩 분리
        word = word + element # word에 요소 담기 
        if word in dic: # 만일 word가 dic의 키에 존재한다면
            answer = answer + str(dic[word]) # 해당 키의 값을 str으로 변환하여 숫자배열에 추가
            word = "" # 임시 배열은 다시 초기화
        if word.isdigit(): # 만일 word가 숫자라면
            answer = answer + word # 문자열인 숫자를 숫자배열에 추가
            word = "" 
    answer = int(answer) # 리턴하기 전에 문자열을 숫자로 형변환
    return answer


solution('2three45sixseven')