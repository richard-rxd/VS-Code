from collections import deque

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
    
    def front(self):
        return self.buffer[-1]
    
def easymode():
    print(bin(numbers.dequeue()).lstrip("0b"))

numbers = queue()

for i in range(1, 11):
    numbers.enqueue(i)

while numbers.is_empty() == False:
    easymode()

# Lösung

def produce_binary_numbers(n):
    numbers_queue = queue()
    numbers_queue.enqueue("1")

    for i in range(n):
        front = numbers_queue.front()
        print("   ", front)
        numbers_queue.enqueue(front + "0")
        numbers_queue.enqueue(front + "1")

        numbers_queue.dequeue()    

if __name__ == '__main__':
    produce_binary_numbers(10)
    k = 10