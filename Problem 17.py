"""
Number letter counts

Problem 17
If the numbers 1 to 5 are written out in words: one, two, three, four, five, then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.

If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, how many letters would be used?


NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and forty-two) contains 23 letters and 115 (one hundred and fifteen) contains 20 letters. The use of "and" when writing out numbers is in compliance with British usage.


Answer:  21124
Completed on Tue, 10 Jul 2018, 19:28
"""

from timeit import default_timer as ti
import os.path as op
from num2words import num2words as n2w


# Solution 1
def numberLetterCount():
    return len(''.join([''.join(sym for sym in n2w(dig) if sym.isalnum()) for dig in range(1,1001)]))


t11 = ti()
print(f"The answer to Project Euler, {op.basename(__file__)[:-3]} is: " + str(numberLetterCount()))
t12 = ti()
print("Time lapsed for solution number 1: " + str((t12-t11)*10**6) + u'\u03BC' + "s")