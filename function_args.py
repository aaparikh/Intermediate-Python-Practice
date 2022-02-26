"""
[1] Difference between arguments and parameters?

[2] Positional and keyword arguments

[3] Default arguments

[4] Variable-length arguments

Container unpacking into function arguments

Local vs global arguments

Parameters passing (by value or by reference)

"""
# [1]
# From a function's perspective:
# A parameter is the variable listed inside the parentheses in the function definition.
# An argument is the value that are sent to the function when it is called.
def print_name(name):
    #name is a parameter
    print(f'bonjour! {name}')

print_name('Atharva')
#here name is a parameter and 'Atharva' is the argument

# [2]
#Positional and keyword arguments
def foo(a,b,c):
    print(a,b,c)

foo(1,2,3) #calling with positional arguments
foo(b=3,a=6,c=2) #calling with keyword arguments (order doesn't matter)
#Note: we can't use a positional argument after a keyword argument

# [3]
# Default parameter should be at the end of the arguments

# [4]
def foo2(a, b, *args, **kwargs):
    #when you mark a parameter with one * then u can pass any number of positional arguments to it
    #when you mark a parameter with two * then u can pass any number of keyword arguments to it
    print(a,b)
    for arg in args:
        print(arg)
    for key in kwargs:
        print(key,kwargs[key])

foo(1,2,3,4,5,h=8,t=0) #here we have passes both positional and keyword arguments

#There are some rules as to howyou have to pass the parameters in the function.
#after dynamic positional arguments, regular positional arguments are not allowed as it confuses the interpreter.

#Unpacking the arguments when passing to a function
def foo3(a,b,c):
    print(a,b,c)

my_list = [1,2,3]
foo3(*my_list) #unpacking

#in case of dictionaries the total length of dict and keys of arguments should match those of parameters
my_dict = {'a':1,'b':2,'c':3}
foo3(**my_dict) #2 astericks are important

#In python call by object or call by object reference is used when passing parameters
#mutable objects can be modified within a function while immutable can't be
#immutable objects can't be changed inside a function and a local variable is thus created

#example mutable objects
def change(l):
    l.append(4)

my_list = [1,2,3]
change(my_list)
print(my_list)
#in this case the passed list was modified


#in this case as we rebinded the definition of l, it was treated as a local variable and
# the original passed list doesn't change
def change2(l):
    l = [1,2,3,4]
    l.append(5)
    l[0] = 788

my_list = [1,2,3]
change2(my_list)

#in short
#mutable objects can be changed
#immutable objects cannot be changed
#but immutable objects contained within mutable objects can be changed
#if reference is rebinded then outer reference will not be changed

#important example
def change_list(l):
    l += [4,5,6] #this will changed the passed list

def change_list2(l):
    l = l + [4,5,6] #this won't change the passed list as a copy is being created

list1 = [1,2,3]
change_list2(list1) #list1 is not changed
change_list(list1) #list1 is changed
