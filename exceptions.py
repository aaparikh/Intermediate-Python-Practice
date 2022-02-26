#Errors and Exceptions

#Syntactical mistakes raise a syntax error
#Exceptions - when sytax is correct but an error is raised it's exception

# different exceptions in python
# https://www.tutorialsteacher.com/python/error-types-in-python

#raising your own exceptions using the raise keyword
x = -10
if x < 0:
    #using the Base exception class
    raise Exception('x should be larger than 0')

#we can also use assertions
assert(x>=0), 'x is not positive' #the string is the message part which will be displayed
#this might prove very useful when debugging

#catching exceptions
try:
    x = 5/0
except Exception as e:
    print(f'An error alien appeared singing - {e}')

#we can use multiple except blocks
#in this case the logic flow will be determoned by the kind of error that occurs
try:
    x = 5 / 0
    b = x + '1'
except ZeroDivisionError as e:
    print(e)
except ValueError as e:
    print(e)
else: #else runs when except and if are not true
    print('Everything is just fine')
finally: #finally runs all the time irrespective of what happened beofer it. Hence cleaning part is usually written here
    print('Cleaning up.....')

#we can also write our own exception classes
class ValueTooHighError(Exception):
    pass

class ValueTooSmallError(Exception):
    def __int__(self,message,value):
        self.message = message
        self.value = value

def test_value(x):
    if x>100:
        raise ValueTooHighError('value is too high')
    if x<5:
        raise ValueTooSmallError('value is too small',x)

test_value(101) #will raise the custom exception

try:
    test_value(50)
except ValueTooHighError as e:
    print(e)
except ValueTooSmallError as e:
    print(e.message,e.value)

