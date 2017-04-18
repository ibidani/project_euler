import math
def is_prime(num):
    for j in range(2,int(math.sqrt(num)+1)):
        if (num % j) == 0:
            return False
    return True

count = 0
sum=0
for i in xrange(1,2000000):
    if is_prime(i):
        sum = sum + i

print sum