#Smallest multiple
#Problem 5

#2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

#What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

#Answer:
#	232792560

# A timer to performance test the solutions
from timeit import default_timer as timer


def div20(nbr):
    c = 0
    while True:
        if nbr % 20 == 0:
            for x in range(19, 2, -1):
                if nbr % x != 0:
                    c = 0
                    break
                else:
                    c +=1
            if c == 17:
                return nbr
        nbr += 19
t1 = timer()
print(div20(19))
t2 = timer()
print("Time taken: " + str((t2-t1)*10**6) + u'\u03BC' + "s")
