"""
Multiples of 3 and 5
Submit

 Show HTML problem content 
Problem 1
If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.


Answer:  233168
Completed on Tue, 12 Mar 2013, 07:46
"""

from timeit import default_timer as timer


# Solution 1
s11 = timer()
print("The answer to Project Euler, problem 1 is: " + str(sum(set([threes for threes in range(0, 1000, 3)] + [fives for fives in range(0, 1000, 5)]))))
s12 = timer()
print("Time lapsed for solution number 1: " + str((s12-s11)*10**6) + u'\u03BC' + "s")
