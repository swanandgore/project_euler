if __name__=="__main__" :
    sqr = lambda x : x*x
    def sum_squares(N) :
        return sum(map(sqr, xrange(1,N+1)))
    def square_sum(N) :
        return sum(xrange(1,N+1)) * sum(xrange(1,N+1))
    N = 100
    print "N = %d, %d - %d = %d" % (N, square_sum(N), sum_squares(N), \
                                        square_sum(N)-sum_squares(N))
