#very imporant concept and every python programmer should know it

#There are two different decorators in python
#1. Function Decorators -> more common
#2. Class Decorators

# Decorator is a function that takes another function as input and extensds the behavior of the function
# without changing the function itself.

#its important to understand that functions in python are class objects.
# This means they can be defined inside another function, passed as argument and returned from another function

def start_n_end(func):
    def wrapper():
        print("Start")
        func()
        print("End")
    return wrapper 

def print_name():
    print("Hello")

print_name() #only prints hello
#adding new functinality to the function
print_name = start_n_end(print_name)
print_name() #prints hello with additional functionality

# This can be done using decorator
# we just won't be needing to write the assignment statement instead we will be using @ symbol
@start_n_end
def print_name():
    print("Hello")

print_name()
#-----------------------------------------------------------------------------------------------------------------------
import functools
from inspect import signature
#passing arguments to the decorator
def start_n_end(func):
    #*args and **kwargs are used to pass arguments to the function
    #*args is used to pass multiple arguments to the function
    #**kwargs is used to pass multiple keyword arguments to the function
    @functools.wraps(func) #preserve the original function information
    def wrapper(*args,**kwargs):
        print("Start")
        result = func(*args,**kwargs)
        print("End")
        return result
    return wrapper

@start_n_end
def add(a,b):
    return (a+b)

print(add(10,20))
print(help(add))
print(add.__name__)
#-----------------------------------------------------------------------------------------------------------------------

#generic template for decorator
def my_decorator(func):
    @functools.wraps(func)
    def wrapper(*args,**kwargs):
        # Do something before
        result = func(*args,**kwargs)
        # Do something after
        return result
    return wrapper
#-----------------------------------------------------------------------------------------------------------------------

#Decorators with arguments
def repeat(n=3):
    def my_decorator(func):
        @functools.wraps(func)
        def wrapper(*args,**kwargs):
            for _ in range(n):
                result = func(*args,**kwargs)
            return result
        return wrapper
    return my_decorator

@repeat(n=5)
def print_name():
    print("Printing something")
#-----------------------------------------------------------------------------------------------------------------------
#Stacking decorators

def add_at_start(func):
    @functools.wraps(func)
    def wrapper(*args,**kwargs):
        print("Today is a good day")
        result = func(*args,**kwargs)
        return result
    return wrapper

def debug(func):
    @functools.wraps(func)
    def wrapper(*args,**kwargs):
        #What is repr and !r -> https://realpython.com/python-f-strings/
        args_repr = [repr(a) for a in args]
        kwargs_repr = [f"{k}={v!r}" for k,v in kwargs.items()]
        signature = ", ".join(args_repr + kwargs_repr)
        print(f'Calling {func.__name__}({signature})')
        result = func(*args,**kwargs)
        print(f'{func.__name__!r} returned {result!r}')
        return result
    return wrapper

@debug
@add_at_start
def say_hello(name):
    greeting = "Hello " + name
    print(greeting)
    return greeting 

#------------------------------------------------------------------------------------------------
# Class Decorators
#do the same stuff as function decorators but are typically used to maintain the state

class CountCalls:
    def __init__(self,func=None) -> None:
        self.func = func
        self.num_calls = 0
    
    def __call__(self, *args, **kwargs):
        self.num_calls += 1
        print(f'This is executed {self.num_calls} times')
        return self.func(*args,**kwargs)

# c = CountCalls()
# c() #we can call class like a function because of the __call__ method present inside it

@CountCalls
def say_something():
    print('Something')

say_something()

#Uses of decorators
#1] Timer dectorators - to calculate the execution time
#2] Debug decorators - to perform proper debugging
#3] Check decorator - to check if the arguments fulfill some requirements