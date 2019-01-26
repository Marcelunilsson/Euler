#10001st prime
#Problem 7

#By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

#What is the 10 001st prime number?

#Answer:
#	104743


# A timer to performance test the solutions
from timeit import default_timer as timer



# Solution 1

# checks if a number is a prime
#def isp(n, lp):
#    c = 0
#    for i in lp:
#        if n % i == 0:
#            return False
#        else:
#            c += 1
#    if c == len(lp):
#        return True

# Adds 10001 first primes to a list
#def p10001():
#    lp = [2]
#    n = 3
#    while len(lp) <= 10000:
#        if isp(n, lp):
#            lp.append(n)
#        else:
#            n += 2
#    return lp[-1]

# main program
#t1 = timer()
#print("Prime number 10001 is: " + str(p10001()))
#t2 = timer()
#print(t2-t1)

# Solution 2

def ps(lim):
    pbl = [True] * lim
    pbl[0] = pbl[1] = False
    c = 0
    for (i, isprime) in enumerate(pbl):
        if isprime:
            c +=1
            if c == 10001:
                return i
            for n in range(i**2, lim, i):
                pbl[n] = False



def isprime(n):
    if n%2 == 0:
        return False
    for i in range(3, int(n**0.5) +1, 2):
        if n%i == 0:
            return False
    return True

t21 = timer()
print(ps(200000))
t22 = timer()
print("Time taken: " + str((t22-t21)*10**6) + u'\u03BC' + "s")
