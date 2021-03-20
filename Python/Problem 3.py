#Largest prime factor
#Problem 3

#The prime factors of 13195 are 5, 7, 13 and 29.

#What is the largest prime factor of the number 600851475143 ?

#Answer:
#	6857



# A timer to performance test the solutions
from timeit import default_timer as timer
import os.path as op

# Solution 1
s11 = timer()
# Divide with all factors to nbr untill only one primefactor is left
nbr = 600851475143
c = 3
while c ** 2 < nbr:
    if nbr % c == 0:
        nbr /= c
    c += 2
print(f"The answer to Project Euler, {op.basename(__file__)[:-3]} is: " + str(int(nbr)))
s12 = timer()
print("Time lapsed for solution number 1: " + str((s12-s11)*10**6) + u'\u03BC' + "s")



# Solution 2
s21 = timer()
# Solution with a vector of primes up to the square root of nbr
import math


# makes a vector of primes up to the square root of the number
def pv():
    n = 5
    pl = [2, 3]
    while n <= math.sqrt(nbr):
        if ip(pl, n) and nbr % n == 0:
            pl.append(n)
            n += 2
        else:
            n += 2
    return pl


# checks if n is a prime
def ip(pl, n):
    c = 0
    for i in range(len(pl)):
        if n % pl[i] == 0:
            c += 1
    if c == 0:
        return True


# Checks what the biggest primefactor in nbr is
def bpinbr():
    pl = pv()
    if ip(pl, nbr):
        return nbr
    for i in pl[::-1]:
        if nbr % i == 0:
            return i


#main program
nbr = 600851475143
#nbr = int(input("For wich number do you want to know the biggest primefactor? : "))
print(f"The answer to Project Euler, {op.basename(__file__)[:-3]} is: " + str(bpinbr()))
s22 = timer()
print("Time lapsed for solution number 2: " + str((s22-s21)*10**6) + u'\u03BC' + "s")


# Solution 3
s31 = timer()
# recursive function

nbr = 600851475143
c = 3
def recbigprime(nbr, c):
    if c ** 2 < nbr and nbr % c != 0:
        recbigprime(nbr, c + 2)
    elif nbr % c == 0 and c ** 2 < nbr:
        nbr /= c
        recbigprime(nbr, c)
    else:
        print(f"The answer to Project Euler, {op.basename(__file__)[:-3]} is: " + str(int(nbr)))
        return True

recbigprime(nbr, c)
s32 = timer()
print("Time lapsed for solution number 3: " + str((s32-s31)*10**6) + u'\u03BC' + "s")
