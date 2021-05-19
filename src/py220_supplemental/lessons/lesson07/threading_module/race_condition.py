#!/usr/bin/env python3

import threading
import time


# create a mutable object that is shared among threads
class shared:
    val = 1
    val2 = 1
    
    def __init__(self, y):
        self.val = y
    
    def func(self):
        # time.sleep(0.1) # self.val = 1
        # time.sleep(0.01) # self.val = 90
        # time.sleep(0.001) # self.val = 95
        time.sleep(0.0001) # self.val = 100
        # time.sleep(0.00001) # self.val = 100
        self.val +=1
        shared.val2 += 1


    
shrek = shared(1)

def func():
    y = shared.val
    # time.sleep(0.1) # shared.val = 2
    # time.sleep(0.01) # shared.val = 8
    # time.sleep(0.001) # shared.val = 18
    time.sleep(0.0001) # shared.val = 28-32
    # time.sleep(0.00001) # shared.val = 28-33
    # time.sleep(0.000001) # shared.val = 58-97
    # time.sleep(0.0000001) # shared.val = 64-98
    # time.sleep(0.00000001) # shared.val = 50-94
    y += 1
    shared.val = y


threads = []
threads_shrek = []
# with enough threads, there's sufficient overhead to
# cause a race condition

# func()
for i in range(100):
    thread = threading.Thread(target=func)
    threads.append(thread)
    thread.start()

# object.func()
for i in range(100):
    thread = threading.Thread(target=shrek.func)
    threads.append(thread)
    thread.start()


print("+++ Class val")
print(shared.val)

print("+++ Class Object val, ")
print(shrek.val)
print(shared.val2)



