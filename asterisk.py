 #different usecases of the * operator

#multiplication
result = 4 * 5
print(result)

#power
result = 4 ** 5
print(result)

#list of repeated elements
l = [1] * 9
# l = [1,2] * 3
# l = (4) * 3
# l = "D" * 6
print(l)

#for args and kwargs
def fun(a,b,*args,**kwargs):
    print(a,b)
    for arg in args:
        print(args)
    for key in kwargs:
        print(key, kwargs[key])
    
fun(1,2,3,4,f=5,g=6)

#all the parameters after * are keyword parameters
def func(a,b,*,c):
    print(a,b,c)
#call should be like this
func(1,2,3,4,5,c=6)#here a=1,b=2, (3,4,5) will be ignored and c=6 has to be specified explicitly (keyword)

#unpacking
def f(a,b,c):
    print(a,b,c)
l1 = ['a','b','c']
f(*l1) #unpacking and passing to function
#while unpacking num of elements = num of parameters

d1 = {'a':1,'b':2,'c':3}
f(**d1)
#length of keys should be same and name of keys should match with parameters

#unpacking containers
lis = [1,2,3,4,5,6,7,8,9]
*beginning, last = list
#in here all the elements except the last one will be assigned to the beginning variable

#merging iterables
my_tuple = (1,2,3)
my_list = [4,5,6]
my_set = {7,8,9}
my_dict1 = {'a':1,'b':2}
my_dict2 = {'c':3,'d':4}
new_list = [*my_tuple,*my_list,*my_set]
new_dict = {**my_dict1,**my_dict2}

