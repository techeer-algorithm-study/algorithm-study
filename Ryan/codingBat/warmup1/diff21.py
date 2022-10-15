""""
Given an int n, return the absolute difference between n and 21, 
except return double the absolute difference if n is over 21.
"""
def diff21(n):
    x = 21 - n
    if n > 21:
        x = x*2
    return abs(x)