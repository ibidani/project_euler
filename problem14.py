def collatz_sequence(x):
    seq = [x]
    if x < 1:
       return []
    while x > 1:
       if x % 2 == 0:
         x = x / 2
       else:
         x = 3 * x + 1
       seq.append(x)    # Added line
    return seq
max_chain_length = 0
max_num = 0
for i in xrange(1,1000000):
    chain_len = len(collatz_sequence(i))
    if chain_len > max_chain_length:
        max_chain_length = chain_len
        max_num = i


print max_chain_length
print max_num