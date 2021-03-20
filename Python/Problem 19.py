"""
Counting Sundays
Submit

 Show HTML problem content 
Problem 19
You are given the following information, but you may prefer to do some research for yourself.

1 Jan 1900 was a Monday.
Thirty days has September,
April, June and November.
All the rest have thirty-one,
Saving February alone,
Which has twenty-eight, rain or shine.
And on leap years, twenty-nine.
A leap year occurs on any year evenly divisible by 4, but not on a century unless it is divisible by 400.
How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?


Answer:  171
"""
from timeit import default_timer as ti
import os.path as op


# Solution 1


t11 = ti()
print(f"The answer to Project Euler, {op.basename(__file__)[:-3]} is: " + str())
t12 = ti()
print("Time lapsed for solution number 1: " + str((t12-t11)*10**6) + u'\u03BC' + "s")