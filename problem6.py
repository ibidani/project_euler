import numpy

def sqrteach(min,max):
    sum = 0
    for i in xrange(min,max):
        sum = sum + numpy.power(i,2)
    return sum

def sqrtall(min,max):
    sum = 0
    for i in xrange(min,max):
        sum = sum + i
    return numpy.power(sum,2)

sumallsqrt = sqrtall(1,101)
sumsqrteach = sqrteach(1,101)

# print sumallsqrt
print sumallsqrt-sumsqrteach