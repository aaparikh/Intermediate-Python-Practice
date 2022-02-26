"""
Context managers are a great tool for resource management, they allow you to allocate and release resources precisely when you want to
"""

#this beautiful code allows context manager to handle all the exception and close the file properly
with open('notes.txt','w') as file:
    file.write('some todo...')

#It is equivalent to writing this line of code
# file  = open('notes.txt','w')
# try:
#     file.write('Some shit..')
# finally:
#     file.close()

#this can also be used with locks
from threading import Lock
lock = Lock()

# lock.acquire()
# ....
# lock.release()

#is equivalent to writing this simple line as
# with lock:
#     ...

#implementing context managers for our own classes
#we have to implement the enter and the exit methods

class ManagedFile:
    def __init__(self,filename) -> None:
        print('init')
        self.filename = filename
    def __enter__(self):
        print('enter')
        self.file = open(self.filename,'w')
        return self.file
    def __exit__(self,exc_type,exc_value,exc_traceback):
        if self.file:
            self.file.close()
        if exc_type: #this handles the exception but we have to return true as otherwise the with statement will raise an exception and stop the execution flow of the program
            print(f'exception : {exc_type} {exc_value} {exc_traceback}') 
        print('exit')
        
with ManagedFile('notes.txt') as file:
    file.write('lolipop ')

#In this way we can implement a context manager using a class


#we can also do this using function
from contextlib import contextmanager
# have to use this as decorator on a generator function

#This functional representatoin is intelligent implementation
@contextmanager
def open_managed_file(filename):
    f = open(filename,'w')
    try: #write the code that would go in the __enter__ method of the class implementation
        yield f
    finally: #write the code that would go in the __exit__ method class implementatoin
        f.close()

with open_managed_file('notes.txt') as f:
    f.write('do something...')