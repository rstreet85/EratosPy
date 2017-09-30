#!/usr/bin/env python
#@author Robert Streetman
#@date   2014-01-07 - Updated 09/15/2017
#@desc   Sieve of Eratosthenes, Python 2.x: Accepts integer n, finds all prime integers from 1 to n; prints largest.

def eratos_old(n):
    """ Older Eratosthenes method, not as Pythonic """
    #TODO:Stop looking for primes halfway between 0-n
    mid = n / 2
    primes = [True] * n

    #Starting at multiples of 2...
    #xrange or enumerate()?
    for num, isPrime in enumerate(primes, start=2):
        #Don't bother finding multiples of x if x isn't a prime
        if isPrime:
            k = 2
	      #Keep from checking for primes above n
            while k * num < n :
                primes[k * num] = False
                k += 1

    #Find first number still prime below n + 1
    index = n - 1
    while index > 0 and primes[index] != True:
        index -= 1
    
    print "The largest prime was: {:,}".format(index)
    
#More pythonic version w/slicing
def eratos(n):
    """ Sieve of Eratosthenes, pythonic """
    

print("This script finds the largest prime integer from 0 to n.")
n = input("Choose limit to search for primes: ") + 1

eratos_old(n)
