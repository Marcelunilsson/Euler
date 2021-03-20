"""
Power digit sum

Problem 16
215 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.

What is the sum of the digits of the number 2^1000?


Answer:  1366
"""
import math
from timeit import default_timer as ti
import os.path as op


# Solution 1
def sumOfDigits(nbr):
    return sum([int(dig) for dig in str(nbr)])

t11 = ti()
print(f"The answer to Project Euler, {op.basename(__file__)[:-3]} is: " + str(sumOfDigits(2**(1000))))
t12 = ti()
print("Time lapsed for solution number 1: " + str((t12-t11)*10**6) + u'\u03BC' + "s")