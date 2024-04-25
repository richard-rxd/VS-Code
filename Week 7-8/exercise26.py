import time
import threading
from threading import Thread

def func_name(x):
    print("Threadnr.: ", x)

threads = []
for i in range(5):
    th = threading.Thread(target=func_name, args=(i,))
    threads.append(th)
    th.start()

for th in threads:
    th.join()


def sleepMe(i):
    print("Thread %i will sleep." % i)
    time.sleep(5)
    print("Thread %i is awake" % i)

for i in range(10):
    th = Thread(target=sleepMe, args=(i, ))
    th.start()
    print("Current Threads: %i." % threading.active_count())
