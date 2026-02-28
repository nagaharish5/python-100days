#https://docs.python.org/3/library/random.html
#https://docs.python.org/3/library/statistics.html
#import random

from numpy.random.mtrand import random_integers
import random
#random.choices(population, weights=None, *, cum_weights=None, k=1);
random_integer= random.randint(0,1000)
#random_number
print(random_integer)


random_number_0_to_10=random.random()
print(random_number_0_to_10)

random_heads_or_tails= random.randint(0,1)
if random_heads_or_tails==0:
    print("Heads")
else:
    print("tails")
#print(random_heads_or_tails)

