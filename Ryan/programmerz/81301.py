# 숫자 문자열과 영단어
# https://school.programmers.co.kr/learn/courses/30/lessons/81301

def solution(s):
    dict_ans = {"zero": 0, "one": 1, "two": 2, "three": 3, "four": 4, "five": 5, "six": 6, "seven": 7, "eight": 8, "nine": 9}
    lst_keys = list(dict_ans.keys())
    temp_answer = ""
    answer = 0
    start = 0
    end = 0
    for i in range(len(s)):
        end = i+1
        check_str = s[start:end]
        if check_str in lst_keys:
            index_lst = lst_keys.index(check_str)
            temp_answer += str(dict_ans[lst_keys[index_lst]])
            start = i+1
        if check_str.isdigit():
            temp_answer += check_str
            start = i+1
    answer = int(temp_answer)
    return answer

def betterSolution(s):
    dict_ans = {"zero": "0", "one": "1", "two": "2", "three": "3", "four": "4", "five": "5", "six": "6", "seven": "7", "eight": "8", "nine": "9"}
    for key, val in dict_ans.items():
        s = s.replace(key, val)
    answer = int(s)
    return answer
