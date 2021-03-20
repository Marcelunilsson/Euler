"""
1000-digit Fibonacci number
Submit

 Show HTML problem content 
Problem 25
The Fibonacci sequence is defined by the recurrence relation:

Fn = Fn−1 + Fn−2, where F1 = 1 and F2 = 1.
Hence the first 12 terms will be:

F1 = 1
F2 = 1
F3 = 2
F4 = 3
F5 = 5
F6 = 8
F7 = 13
F8 = 21
F9 = 34
F10 = 55
F11 = 89
F12 = 144
The 12th term, F12, is the first term to contain three digits.

What is the index of the first term in the Fibonacci sequence to contain 1000 digits?


Answer:  4782
"""

from timeit import default_timer as ti
import os.path as op


# Solution 1


t11 = ti()
print(f"The answer to Project Euler, {op.basename(__file__)[:-3]} is: " + str())
t12 = ti()
print("Time lapsed for solution number 1: " + str((t12-t11)*10**6) + u'\u03BC' + "s")