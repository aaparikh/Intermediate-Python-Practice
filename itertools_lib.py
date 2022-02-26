#itertools
# https://www.geeksforgeeks.org/python-itertools/

#product
from itertools import product
#computes the cartesian product
a = [1,2]
b = [3,4]
d = product(a,b)
print(list(d)) #[(1, 3), (1, 4), (2, 3), (2, 4)]
d2 = product(a,b,repeat=2) #do this twice
print(list(d2)) #[(1, 3), (1, 4), (2, 3), (2, 4)] * [(1, 3), (1, 4), (2, 3), (2, 4)] -> 16 elements

#permutations -> arrangements
from itertools import permutations
a = [1,2,3]
pm = permutations(a,2) #r is length of each paermutation
print(list(pm))
#[(1, 2), (1, 3), (2, 1), (2, 3), (3, 1), (3, 2)]

#combinations -> selections
from itertools import combinations, combinations_with_replacement
a = [1,2,3]
cn = combinations(a,2)
print(list(cn))
#[(1, 2), (1, 3), (2, 3)]

cn2 = combinations_with_replacement(a,2) #repetition allowed
print(list(cn2))
#[(1, 1), (1, 2), (1, 3), (2, 2), (2, 3), (3, 3)]

#accumulate
from itertools import accumulate
import operator
#get the running sum
a = [1,2,3,4]
add_a = accumulate(a)
print(list(add_a)) #[1,3,6,10]
mul_a = accumulate(a,func=operator.mul)
print(list(mul_a)) #[1,2,6,24]

from itertools import groupby

a = [1,2,3,4,5,6]
groub_obj = groupby(a,key=lambda x:x<3)
# print(list(groub_obj))
for key, value in groub_obj:
    print(key, list(value))
#True [1, 2]
# False [3, 4, 5, 6]

#infinite iterators
from itertools import count, cycle, repeat
#count, cycle, repeat
for i in count(10):
    print(i)
    if(i==15):
        break
#count starts the loop at 10 and goes on till infinity

a = [1,2,3,4]
for i in cycle(a):
    print(i)
    if(i==4):
        break
#cycle will keep iterating and reiterating over the iterable

for i in repeat(2):
    print(i)
    break
#repeat just repeats the number 2 till infinity

