# MULTIPROCESSING
import imp
from multiprocessing import Process
import os

print(f'There are {os.cpu_count()} on your device')

processes = []
#It is a good idea to create num of processes equal to cpu count on your device
num_processes = os.cpu_count()

def sq():
    for i in range(100):
        i * i

#create processes
for i in range(num_processes):
    p = Process(target=sq)
    processes.append(p)

for p in processes:
    p.start()

#Now wait for the process to finish and while waiting block the main thread
for p in processes:
    p.join()

#--------------------------------------------------------------------------------------------------------------------
# MULTITHREADING
from threading import Thread

threads = []
num_of_threads = 10

def sqr():
    for i in range(10):
        i ** (1/2)

for n in range(num_of_threads):
    t = Thread(target=sqr)
    threads.append(t)

for t in threads:
    t.start()
for t in threads:
    t.join()
print('End threads')