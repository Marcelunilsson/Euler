#Sum square difference
#Problem 6

#The sum of the squares of the first ten natural numbers is,
#12 + 22 + ... + 102 = 385

#The square of the sum of the first ten natural numbers is,
#(1 + 2 + ... + 10)2 = 552 = 3025

#Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025 − 385 = 2640.

#Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.

#Answer:
#	25164150

# A timer to performance test the solutions
from timeit import default_timer as timer
import os.path as op
# Solution 1
def sql(vec):
    return map(lambda x: x**2, vec)
t11 = timer()
vec = range(101)
vecsq = sql(vec)

print(f"The answer to Project Euler, {op.basename(__file__)[:-3]} is: " + str(sum(vec)**2 - sum(vecsq)))
t12 = timer()
print("Time lapsed for solution number 1: " + str((t12-t11)*10**6) + u'\u03BC' + "s")
