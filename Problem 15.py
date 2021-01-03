"""
Lattice paths
Submit

 Show HTML problem content 
Problem 15
Starting in the top left corner of a 2×2 grid, and only being able to move to the right and down, there are exactly 6 routes to the bottom right corner.


How many such routes are there through a 20×20 grid?


Answer:  137846528820
Completed on Sun, 8 Jul 2018, 15:46
"""
import math
from timeit import default_timer as ti


# Solution 1
def latticePaths(n, m):
    return int(math.factorial(n+m) / (math.factorial(n)*math.factorial(m)))

t11 = ti()
print("The answer to Project Euler, problem 15 is: " + str(latticePaths(20, 20)))
t12 = ti()
print("Time lapsed for solution number 1: " + str((t12-t11)*10**6) + u'\u03BC' + "s")