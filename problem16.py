import math

sum_result = int(math.pow(2,1000))

sum_digits = 0
while sum_result:
    sum_digits += sum_result % 10

    sum_result //= 10

print sum_digits