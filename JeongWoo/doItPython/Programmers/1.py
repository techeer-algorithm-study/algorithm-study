dict = {'zero' : 0,'one' : 1,'two' : 2,'three' : 3,'four' : 4,'five' : 5,'six' : 6, 'seven' : 7,'eight' : 8,'nine' : 9}

def solution(s):
    result = ""
    word = ""
    for element in s:
        word = word + element
        if word in dict:
            result = result + str(dict[word])
            word = ""
        if word.isdigit(): 
            result = result + word
            word = "" 
    return int(result)


solution('2three45sixseven')