"""
Given an int n, return True if it is within 10 of 100 or 200.
 Note: abs(num) computes the absolute value of a number.
"""
def near_hundred(n):
    x = abs(100-n)
    y = abs(200-n)
    return (x <= 10 or y <= 10)
