#Special Pythagorean triplet
#Problem 9

#A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
#a2 + b2 = c2

#For example, 32 + 42 = 9 + 16 = 25 = 52.

#There exists exactly one Pythagorean triplet for which a + b + c = 1000.
#Find the product abc.

#Answer:
#	31875000


# A timer to performance test the solutions
from timeit import default_timer as ti
import os.path as op

# numpy to make calculations
#import numpy as np


# Solution 1
def fpt1000():
    for z in range(800, 1, -1):
        for y in range(300, z):
            for x in range(200, y):
                if x < y < z and x + y + z == 1000:
                    if x**2 + y**2 == z**2:
                        print(f"The answer to Project Euler, {op.basename(__file__)[:-3]} is: " + "abc = " + str(x * y * z))
                        print("                                           a =" + str(x) + ", b =" + str(y) + ", c =" + str(z))
    return True
t11 = ti()
fpt1000()
t12 = ti()
print("Time lapsed for solution number 1: " + str((t12-t11)*10**6) + u'\u03BC' + "s")
