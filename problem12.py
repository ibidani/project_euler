import math
import numpy as np

def divisorGenerator(n):
    large_divisors = []
    for i in xrange(1, int(math.sqrt(n) + 1)):
        if n % i == 0:
            yield i
            if i*i != n:
                large_divisors.append(n / i)
    for divisor in reversed(large_divisors):
        yield divisor

# print len(list(divisorGenerator(28)))
tri_num_start = 1
tri_num_end = 1000000000
for i in xrange(tri_num_start+1,tri_num_end+2):
    tri_num = np.sum(xrange(1,i))
    divisors_num = len(list(divisorGenerator(tri_num)))
    if divisors_num >= 500:
        print "first triangle number to have over five hundred divisors"+str(tri_num)
        print divisors_num
        print i
        break
