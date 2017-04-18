import math
for a in xrange(1000):
    for b in xrange(500):
        for c in xrange(500):
            asq = (a ** 2)
            bsq = (b ** 2)
            if c**2 == asq + bsq:
                # print 'a:'+str(a)+'b:'+str(b)+'c:'+str(c)
                if (a < b) and (b < c):
                    if a + b + c == 1000:
                        print 'a:'+str(a)+'b:'+str(b)+'c:'+str(c)
                        break
