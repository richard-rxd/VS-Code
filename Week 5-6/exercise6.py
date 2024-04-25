from collections import deque
import time
import threading

class queue:
    
    def __init__(self):
        self.buffer = deque()
    
    def enqueue(self, val):
        self.buffer.appendleft(val)
        
    def dequeue(self):
        return self.buffer.pop()
    
    def is_empty(self):
        return len(self.buffer)==0
    
    def size(self):
        return len(self.buffer)
    
def placeorder(orders):
    for i in orders:
        time.sleep(0.5)
        preparing.enqueue(i)
        print(f" Order for: {i} has been accepted")

def serveorder():
    time.sleep(1)
    while preparing.is_empty() == False:
        x = preparing.dequeue()
        print(f"{x} has been served")
        time.sleep(1)
    
preparing = queue()
orders = ['pizza','samosa','pasta','biryani','burger']

t1 = threading.Thread(target = placeorder, args = (orders,))
t2 = threading.Thread(target = serveorder)

t1.start()
t2.start()

t1.join()
t2.join()

print("Orders finished")