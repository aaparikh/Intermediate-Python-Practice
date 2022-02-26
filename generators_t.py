#The generate items one at a time when you asl for it
#thus they are memory efficient and very useful

#If the body of a def contains yield, the function automatically becomes a generator function.
#what yield does is pauses and return the value and then resumes it at the next function call
def my_generator():
    yield 1
    yield 2
    yield 3

g1 = my_generator()
print(g1)
for x in g1:
    print(x)

# print(next(g1)) #object will be empty
#generator object will always raise a StopIteration error if it does not reach another yrild statement

#analysis the efficiency
from re import A
import sys
def get_n(n) -> list:
    l = []
    num = 0
    while num < n:
        l.append(num)
        num += 1
    return l

def get_n_generator(n) -> None:
    num = 0
    while num < n:
        yield num
        num += 1

print(f'List method takes - {sys.getsizeof(get_n(1000))} bytes of memory')
print(f'List method takes - {sys.getsizeof(get_n_generator(1000))} bytes of memory')

def fibonacci(limit):
    a, b = 0,1
    while a < limit:
        yield a
        a,b = b, a+b

fib = fibonacci(30)
for i in fib:
    print(i)

#---------------------------------------------------------------------------------------------------
#creating generators directly
mygenerator = (i for i in range(20) if i%2==0)
print(mygenerator)