"""
Factorial digit sum
Submit

 Show HTML problem content 
Problem 20
n! means n × (n − 1) × ... × 3 × 2 × 1

For example, 10! = 10 × 9 × ... × 3 × 2 × 1 = 3628800,
and the sum of the digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.

Find the sum of the digits in the number 100!


Answer:  648
Completed on Fri, 24 Aug 2018, 09:07
"""
from timeit import default_timer as ti
import os.path as op


# Solution 1


t11 = ti()
print(f"The answer to Project Euler, {op.basename(__file__)[:-3]} is: " + str())
t12 = ti()
print("Time lapsed for solution number 1: " + str((t12-t11)*10**6) + u'\u03BC' + "s")