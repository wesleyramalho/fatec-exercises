# from numpy.random import seed
# from numpy.random import randint
# seed random number generator
# seed(1)
# generate some integers
# values = randint(0, 10, 20)
# import random
# values = random.randrange(8923483)  
# print(values)


from random import randint

def random_with_N_digits(n):
    range_start = 10**(n-1)
    range_end = (10**n)-1
    return randint(range_start, range_end)

print(random_with_N_digits(2))
print(random_with_N_digits(3))
print(random_with_N_digits(4))