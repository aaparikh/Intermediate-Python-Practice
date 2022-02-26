from threading import Thread, Lock
import time

#as all the threads use same memory its easy to share memory between them
database_value = 0

def increase(lock):
    #this is done to simulate a real scenario of changing values in a database
    
    lock.acquire() #now the thread will not be switched as its state is locked
    #Note : always remember to release the resource which you have locked or the code will be stuck there itself
    global database_value
    local_cpy = database_value
    #do some processing 
    local_cpy += 1
    time.sleep(0.1)
    database_value = local_cpy
    lock.release()

    # there is another way to write this 
    # with lock:
    #     global database_value
    #     local_cpy = database_value
    #     #do some processing 
    #     local_cpy += 1
    #     time.sleep(0.1)
    #     database_value = local_cpy
    # in this the context manager acquires and releases the lock for you


print('start value ',database_value)
#locks are added to prevent race condition (race condition = multiple threads writing the same resource)
lock = Lock()
thread1 = Thread(target=increase,args=(lock,))
thread2 = Thread(target=increase,args=(lock,))

thread1.start()
thread2.start()

thread1.join()
thread2.join()

print('End value ',database_value)

#-----------------------------------------------------------------------------------------------------------------------------
#Using Queues

from queue import Queue
#follows FIFO -> First In First Out

from threading import current_thread #to get info about current thread

def worker(q,lock):
    while True:
        value = q.get()
        #processing...
        with lock:
            print(f'in {current_thread().name} got {value}')
        q.task_done()
#using queue is thread safe
q = Queue()
lock = Lock()
num_threads = 10
for thread in range(num_threads):
    t = Thread(target=worker,args=(q,lock))
    t.daemon = True
    t.start()

#Now fill the queue
for i in range(21):
    q.put(i)

q.join()
print('End process') 
#Deamon thread dies when the main thread dies. So the infinite loop is exited 