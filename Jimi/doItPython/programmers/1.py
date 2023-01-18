dic = {'zero':0, 'one':1, 'two':2, 'three':3, 'four':4, 'five':5, 'six':6, 'seven':7, 'eight':8, 'nine':9}

def solution(s):
    answer = ""
    word = ""
    for element in s:
        word = word + element
        if word in dic:
            answer = answer + str(dic[word])
            word = ""
        if word.isdigit():
            answer = answer + word
            word = ""
    answer = int(answer)
    return answer

    
solution('2three45sixseven')