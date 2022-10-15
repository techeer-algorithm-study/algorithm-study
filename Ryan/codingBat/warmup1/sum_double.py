"""
Given two int values, return their sum. 
Unless the two values are the same, then return double their sum.
"""
def sum_double(a, b):
    c = a+b
    if a == b:
        return 2*c
    else:
        return c