"""Given a string, return a new string where "not " has been added to the front. 
However, if the string already begins with "not", return the string unchanged.
"""
def not_string(str):
    f3 = str[0:3]
    if f3 != "not":
        return "not "+str
    return str