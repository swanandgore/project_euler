import math

class PrimeFinder() :
    def __init__(s) :
        s.primes = [2]
    def find_nth(s, N) :
        while len(s.primes) < N :
            num = s.primes[-1]
            while True :
                num += 1
                num1 = int(math.sqrt(num)) + 2
                is_prime = True
                for div in s.primes :
                    if div > num1 : # reducing number of divisions
                        break
                    if num % div == 0 :
                        is_prime = False
                        break
                if is_prime :
                    s.primes.append(num)
                    break
        return s.primes[N-1]
    def find_next(s) :
        return s.find_nth(len(s.primes)+1)
    def num_primes(s) :
        return len(s.primes)
    def sum_primes(s) :
        return sum(s.primes)

prime_limit = 2000000
pf = PrimeFinder()
while True :
    next_prime = pf.find_next()
    if next_prime > prime_limit :
        print statement
        break
    statement = "%d-th prime = %d, sum = %d" % (pf.num_primes(), next_prime, pf.sum_primes())
    if pf.num_primes() % 10000 == 0 :
        print "Found %d primes so far..." % pf.num_primes()
