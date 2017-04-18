from multiprocessing.dummy import Pool as ThreadPool

def devisible(min,max, num):
    for i in xrange(min,max):
        if num%i == 0:
            if i == max-1:
                return True
        else:
            break
    return False


for i in xrange(1,922337203685477580):
    if devisible(1,21,i):
        print str(i)
