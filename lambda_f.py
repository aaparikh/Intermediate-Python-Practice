#lambda are one line functions
add5 = lambda x:x+5
print(add5(10))

points2D = [(-1,21),(9,4),(-5,6),(5,8),(19,-10)]
points2D_sorted = sorted(points2D,key=lambda x:x[1])
#by default it is sorted by the first argument
#we change that behaviour using lambda function
print(points2D_sorted)

from functools import reduce
b = [1,2,3,4,5]
sq_b = list(map(lambda x:x**2, b))
print(sq_b)

even_b = list(filter(lambda x:x%2==0,b))
print(even_b)

red_b = reduce(lambda x,y:x*y,b)
print(red_b)