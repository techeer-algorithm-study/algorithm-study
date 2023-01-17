# k번째 수
# https://school.programmers.co.kr/learn/courses/30/lessons/42748

def solution(array, commands):
    #commands is nested list
    n = len(commands)
    answer = [0]*n
    for items in range(n):
        i,j,k = commands[items]
        answer[items] = sorted(array[i-1:j])[k-1]
    return answer
