import threading
import time


# create a mutable object that is shared among threads
class Shared:
    val = 1


def func():
    y = Shared.val
    time.sleep(0.00001)
    y += 1
    Shared.val = y


threads = []
for i in range(99):
    thread = threading.Thread(target=func)
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()

print(Shared.val)
