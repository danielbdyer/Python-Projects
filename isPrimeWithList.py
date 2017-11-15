from checkint import numbercheck


def isPrime(n):
    primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
    x = 0
    for prime in primes:
        if n == prime:
            print "This is a prime number!"
            return True
        elif n % prime == 0:
            print "{0} is not a prime number, as it is divisible by {1}".format(n,primes[x])
            return False
        else:
            print "This is likely a prime number!"
            return True
        x += 1

n = int(numbercheck("Would you like to see if a number is prime? Enter it now: "))
isPrime(n)
