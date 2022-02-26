#How can we share data between processes?
# Processes don't live in the same memory,  so they don't have access to same public data and need special access
# to shared memory data. There are two shared memory objects that we can use.
#1] Value
#2] Array

from multiprocessing import Process, Value, Array, Lock
import numbers
import os
import time

def add100(num,lock):
    time.sleep(0.01) #when locks are not applied process swithching will take place here
    for i in range(100):
        with lock:
            num.value += 1

def sum_array(arr,lock):
    time.sleep(0.01)
    #each thread will add 100 to each number in the shared array
    #so 2 threads means 200 will be added to each number of the array
    for i in range(100):
        for i in range(len(arr)):
            with lock:
                arr[i] += 1

def square(numbers,q):
    for i in numbers:
        q.put(i*i)

def make_negative(numbers,q):
    for i in numbers:
        q.put(-1*i)

def cube(number):
    return number**3

if __name__ == '__main__':
    lock = Lock()
    #here we create a shared variable which can be accessed by all the processes
    shared_number = Value('i',0) #starting value is 0 and is of type int (i)
    print(f'Number at beginning is {shared_number.value}')

    p1 = Process(target=add100,args=(shared_number,lock))
    p2 = Process(target=add100,args=(shared_number,lock))

    p1.start()
    p2.start()

    p1.join()
    p2.join()

    print(f'Number at end is {shared_number.value}')

    #for a shared Array
    array = Array('d',[1.4,2.2,3.4,4.6,5.8])
    print(f'Array at beginning is {array[:]}')
    p1 = Process(target=sum_array,args=(array,lock))
    p2 = Process(target=sum_array,args=(array,lock))

    p1.start()
    p2.start()

    p1.join()
    p2.join()

    print(f'Array at end is {array[:]}')

    #------------------------------------------------------------------------------------------
    from multiprocessing import Queue

    q = Queue()

    p1 = Process(target=square,args=(numbers,q))
    p2 = Process(target=make_negative,args=(numbers,q))

    p1.start()
    p2.start()

    p1.join()
    p2.join()

    while not q.empty():
        print(q.get())
    #Both processors will have access to the queue

#A process pool is used to contorl multiple processes
# A process pool object controls a pool of worker processes to which jobs can be submitted
#then it can use the available processors for you and for example split data into smaller chunks which 
# can then be processed in parallel by different processors

from multiprocessing import Pool
pool = Pool()
numbers = range(10)
#4 important methods (there are more but these are mostlt used)
#map, apply, join, close
result = pool.map(cube,numbers) #This will automatically divide the work among processors and split the iterable into equal chunks and allocate to the processors
pool.apply(cube,numbers[0]) #execute the process with 
pool.close() #remember to do this
pool.join() #wait for pool to process all calculations and return results
print(result)

