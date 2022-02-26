#there are many ways we can do random numbers

#1. import random
#used to produce pseudo-random numbers. 
# They are called pseudo-random because they are not truly random and can be reproduced.
import random

a = random.random() #random float between 0 and 1
b = random.uniform(1,10) #random float between 1 and 10
c = random.randrange(1,10) #random integer between 1 and 10 (not including 10)
d = random.randint(1,10) #random integer between 1 and 10 (including 10)
e = random.choice(['a','b','c']) #random element from a list
#sample picks one element one time and choices may pick one element multiple times
f = random.sample(range(1,10),3) #3 random elements from a list
g = random.choices(range(1,10),k=3) #3 random elements from a list
h = random.normalvariate(0,1) #random float from normal distribution with mean 0 and standard deviation 1
random.shuffle(['a','b','c']) #shuffle a list in place
random.seed(10) #set the seed for the random number generator to 10 (so that the same sequence of numbers will be generated)


import secrets #secrets — Generate secure random numbers for managing secrets (True randomness)
# https://docs.python.org/3/library/secrets.html
#But this is slower than random module as more complex algorithms are used.

a = secrets.randbelow(10) #random integer between 0 and 9
b = secrets.randbits(10) #random integer between 0 and 2**10-1
c = secrets.choice(['a','b','c']) #random element from a list
d = secrets.sample(range(1,10),3) #3 random elements from a list


#2. import numpy
import numpy as np
#numpy random generator uses a different generator than random module and also has a different seed
np.random.seed(10) #set the seed for the random number generator to 10 (so that the same sequence of numbers will be generated)
a = np.random.random() #random float between 0 and 1
b = np.random.uniform(1,10) #random float between 1 and 10
c = np.random.randrange(1,10) #random integer between 1 and 10 (not including 10)
d = np.random.randint(1,10) #random integer between 1 and 10 (including 10)
e = np.random.choice(['a','b','c']) #random element from a list
f = np.random.randn(3) #list of 3 random elements 