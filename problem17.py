import num2words
import re

sum_letters = 0
for i in xrange(1,1001):
    sum_letters += len(re.sub(r'\W+','',num2words.num2words(i)))
    print i
print sum_letters
# print num2words.num2words(342)
# print "three hundred and forty-two".replace(' ','').replace('-','')
# print len(num2words.num2words(342).replace(' ','').replace('-',''))