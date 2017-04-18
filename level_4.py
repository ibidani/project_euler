def is_palindrome(i):
    if str(i) == str(str(i)[::-1]):
        return True
    else:
        return False


for i in xrange(900,1000):
    for j in xrange(900,1000):
        num = i*j
        if is_palindrome(num):
            print str(i) +','+str(j)+'='+str(num)

