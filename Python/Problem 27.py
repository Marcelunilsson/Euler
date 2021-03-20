"""
Quadratic primes

Problem 27
Euler discovered the remarkable quadratic formula: n^2 + n + 41


It turns out that the formula will produce 40 primes for the consecutive integer values 0=< n =< 39 . However, when n = 40  is divisible by 41, 
and certainly when n = 41  is clearly divisible by 41.

The incredible formula n^2 -79n + 1601 was discovered, which produces 80 primes for the consecutive values 0=< n =< 79. The product of the coefficients, −79 and 1601, is −126479.

Considering quadratics of the form:
n^2 + an + b , where |a| < 1000 and |b| < 1000

where |n| is the modulus/absolute value of n 
e.g. |11| = 11 and |-4|= 4
Find the product of the coefficients, a and b, for the quadratic expression that produces the maximum number of primes for consecutive values of n, starting with n=0.
"""


from timeit import default_timer as ti
import os.path as op

# Solution 1


t11 = ti()
print(f"The answer to Project Euler, {op.basename(__file__)[:-3]} is: " + str())
t12 = ti()
print("Time lapsed for solution number 1: " + str((t12-t11)*10**6) + u'\u03BC' + "s")