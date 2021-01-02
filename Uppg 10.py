
#Summation of primes
#Problem 10

#The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

#Find the sum of all the primes below two million.

#Answer:
#	142913828922



# A timer to performance test the solutions
from timeit import default_timer as ti

# numpy to make calculations
#import numpy as np


# Solution 1

def ps(lim):
    pbl = [True] * lim
    pbl[0] = pbl[1] = False
    for (i, isprime) in enumerate(pbl):
        if isprime:
            yield i
            for n in range(i**2, lim, i):
                pbl[n] = False

t11 = ti()
print("The answer to Project Euler, problem 10 is: " + str(sum(ps(2*10**6))))
t12 = ti()
print("Time lapsed for solution number 1: " + str((t12-t11)*10**6) + u'\u03BC' + "s")