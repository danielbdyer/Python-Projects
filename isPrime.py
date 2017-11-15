from checkint import numbercheck
import math

def isPrime(n):
    if n < 2:
        print "Numbers less than two cannot be prime."
        return False
    else:
        for i in range(2, int(math.sqrt(n))):
            if n % i == 0:
                print "{0} is divisible by {1}, so it is not prime.".format(n,i)
                return False
        print "This is likely a prime number. Good find!"
        return True

n = int(numbercheck("What number would you like to check for prime? "))
isPrime(n)
