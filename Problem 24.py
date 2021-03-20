"""
Lexicographic permutations
Submit

 Show HTML problem content 
Problem 24
A permutation is an ordered arrangement of objects. For example, 3124 is one possible permutation of the digits 1, 2, 3 and 4. If all of the permutations are listed numerically or alphabetically, we call it lexicographic order. The lexicographic permutations of 0, 1 and 2 are:

012   021   102   120   201   210

What is the millionth lexicographic permutation of the digits 0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?


Answer:  2783915460
Completed on Sat, 14 Mar 2020, 11:54
"""

from timeit import default_timer as ti
import os.path as op

# Solution 1


t11 = ti()
print(f"The answer to Project Euler, {op.basename(__file__)[:-3]} is: " + str())
t12 = ti()
print("Time lapsed for solution number 1: " + str((t12-t11)*10**6) + u'\u03BC' + "s")