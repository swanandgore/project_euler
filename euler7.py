import math

class PrimeFinder() :
    def __init__(s) :
        s.primes = [2]
    def find_nth(s, N) :
        while len(s.primes) < N :
            num = s.primes[-1]
            while True :
                num += 1
                if all((num % div != 0 for div in s.primes)) :
                    s.primes.append(num)
                    break
        return s.primes[N-1]

pf = PrimeFinder()
for n in range(1,10002) :
    print n, pf.find_nth(n)
