#Largest palindrome product
#Problem 4

#A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

#Find the largest palindrome made from the product of two 3-digit numbers.

#Answer:
#	906609

# A timer to performance test the solutions
from timeit import default_timer as timer

# multiplier
def mp(sr):
    bp = 0
    for x in range(999, 999-sr, -1):
        for y in range(999, 999-sr, -1):
            if cip(x* y) and x*y >= bp:
                bp = x * y
    if bp == 0:
        bp = mp(sr + 20)
    return bp

# check if palindrome
def cip(n):
    ns = str(n)
    if len(ns) == 6 and ns[0] == ns[5] and ns[1] == ns[4] and ns[2] == ns[3]:
        return True
    else:
        return False

# main program
t1 = timer()
sr = 10
print(mp(sr))
t2 = timer()
print("Time taken: " + str((t2-t1)*10**6) + u'\u03BC' + "s")
