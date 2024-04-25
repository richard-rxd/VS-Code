import os

# Task 1

jantem = [27, 31, 23, 34, 37, 38, 29, 30, 35, 30]

avg = 0
sum = 0

for i in range(7):
    sum += jantem[i]

avg = sum/7

max = -276

for items in jantem:
    if max < items:
        max = items

print(f"AVG: {avg} ; MAX: {max}")

# Task 2

class temtable:
    def __init__(self):
        self.max = 30
        self.arr = [[] for i in range(self.max)]

    def get_hash(self, date):
        h = 0
        for char in date: 
            h += ord(char)
        return h % self.max
    
    def __setitem__(self, date, temp):
        h = self.get_hash(date)
        
        if len(self.arr[h]) != 0:
            for i, elements in self.arr[h]:
                if len(elements) == 2 and elements[0] == date:
                    self.arr[h][i] = (date, temp)
                    return
        
        self.arr[h].append((date, temp))

    def __getitem__(self, date):
        h = self.get_hash(date)

        if len(self.arr[h]) > 2:
            for i, elements in self.arr[h]:
                if elements[0] == date:
                    return self.arr[h][i][1]
            
        return self.arr[h][0][1]

nyc_weather = temtable()

with open(os.path.join(os.path.dirname(__file__), "nyc_weather.csv") , "r") as source: 
    next(source)
    for line in source:
        data = line.split(",")
        nyc_weather[data[0]] = int(data[1])

print(f"Temperature on Jan 9 was {nyc_weather["Jan 9"]} ")
print(f"Temperature on Jan 7 was {nyc_weather["Jan 7"]} ")
print(f"Temperature on Jan 5 was {nyc_weather["Jan 5"]} ")
print(f"Temperature on Jan 4 was {nyc_weather["Jan 4"]} ")
print(f"Temperature on Jan 3 was {nyc_weather["Jan 3"]} ")
print(f"Temperature on Jan 2 was {nyc_weather["Jan 2"]} ")
print(f"Temperature on Jan 1 was {nyc_weather["Jan 1"]} ")