def is_prime(x):
    for n in range(2,x):
        if x % n == 0:
           return False
    return True

count = 0
for i in xrange(1,922337203685477580):
    if is_prime(i):
        if count % 100 == 0:
            print 'prime no.'+str(count)+'-'+str(i)

        if count == 10001:
            print 'prime no.'+str(count)+'-'+str(i)
            break
        count = count + 1