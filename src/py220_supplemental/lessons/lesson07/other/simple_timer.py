import threading
import time

def called_once():
    """
    this function is designed to be called once in the future
    """
    print("I just got called! It's now: {}".format(time.asctime()))

# setting it up to be called
t = threading.Timer(interval=3, function=called_once)
t.start()

# you can cancel it if you want:
t.cancel()