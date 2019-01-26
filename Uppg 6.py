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


def sql(vec):
    return map(lambda x: x**2, vec)
t1 = timer()
vec = range(101)
vecsq = sql(vec)

print(sum(vec)**2 - sum(vecsq))
t2 = timer()
print("Time taken: " + str((t2-t1)*10**6) + u'\u03BC' + "s")
