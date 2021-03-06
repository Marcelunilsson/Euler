"""
Longest Collatz sequence
Submit

 Show HTML problem content 
Problem 14
The following iterative sequence is defined for the set of positive integers:

n → n/2 (n is even)
n → 3n + 1 (n is odd)

Using the rule above and starting with 13, we generate the following sequence:

13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1
It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. Although it has not been proved yet (Collatz Problem), 
it is thought that all starting numbers finish at 1.

Which starting number, under one million, produces the longest chain?

NOTE: Once the chain starts the terms are allowed to go above one million.


Answer:  837799
Completed on Wed, 4 Jul 2018, 14:17
"""

from timeit import default_timer as ti
import os.path as op

# Solution 1
t11 = ti()
biggestNbr, largestChain = 0, 0
for startNbr in range(10**6, 8*10**5, -1):
    nbr, count = startNbr, 0
    while nbr > 1:
        count += 1
        if nbr % 2:
            nbr = 3*nbr + 1
        else:
            nbr = nbr/2
    if count > largestChain:
        largestChain = count
        biggestNbr = startNbr

print(f"The answer to Project Euler, {op.basename(__file__)[:-3]} is: " + str(biggestNbr))
t12 = ti()
print("Time lapsed for solution number 1: " + str((t12-t11)*10**6) + u'\u03BC' + "s")