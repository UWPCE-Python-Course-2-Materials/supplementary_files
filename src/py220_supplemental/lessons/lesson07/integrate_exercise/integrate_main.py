#!/usr/bin/env python

import threading
import queue
import time

from integrate import integrate_numpy, f

def timer(func):
    def wrapper(*arg, **kw):
        '''
        Secondary source: https://stackoverflow.com/questions/1622943/timeit-versus-timing-decorator
        Primary source: http://www.daniweb.com/code/snippet368.html
        '''
        t1 = time.time()
        res = func(*arg, **kw)
        t2 = time.time()
        total_time = t2 - t1
        print(f"Total time: {total_time} seconds")
        return res
    return wrapper

@timer
def threading_integrate(f, a, b, N, thread_count=2):
    """break work into N chunks"""
    N_chunk = int(float(N) / thread_count)
    dx = float(b - a) / thread_count

    results = queue.Queue()

    def worker(*args):
        results.put(integrate_numpy(*args))

    for i in range(thread_count):
        x0 = dx * i
        x1 = x0 + dx
        thread = threading.Thread(target=worker, args=(f, x0, x1, N_chunk))
        thread.start()
        print("Thread %s started" % thread.name)

    return sum((results.get() for i in range(thread_count)))


if __name__ == "__main__":

    # parameters of the integration
    a = 0.0
    b = 10.0
    N = 10**8
    thread_count = 8

    print("Numerical solution with N=%(N)d : %(x)f" %
          {'N': N, 'x': threading_integrate(f, a, b, N, thread_count=thread_count)})
