import threading

class MyThread(threading.Thread):

    def run(self):
        print("hello from %s" % threading.current_thread().name)

thread = MyThread()
thread.start()