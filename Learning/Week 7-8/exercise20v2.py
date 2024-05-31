class ReachedLimit(Exception):
    pass

class primenumb:
    def __init__(self, limit):
        self.limit = limit
        self.n = 0
        self.current = 1

    def __iter__(self):
        return self
    
    def __next__(self):
        while True:
            self.current += 1
            if self.isprime(self.current):
                self.n += 1
                if self.n <= self.limit:
                    return self.current
                else:
                    raise ReachedLimit

    def isprime(self, num):
        if num <= 1:
            return False
        if num <= 3:
            return True
        if num % 2 == 0 or num % 3 == 0:
            return False
        i = 5
        while i * i <= num:
            if num % i == 0 or num % (i + 2) == 0:
                return False
            i += 6
        return True

primeiter = iter(primenumb(10))

while True:
    try:
        print(next(primeiter))
    except ReachedLimit:
        break