class hashtable:
    def __init__(self):
        self.max = 10
        self.arr = [None for i in range(self.max)]

    def get_hash(self, key):
        h = 0
        for char in key: 
            h += ord(char)
        return h % self.max
    
    def __setitem__(self, key, value):
        h = self.get_hash(key)

        if self.arr[h] != None:
            for i in range(1, self.max):
                index = (h + i) % self.max
                if self.arr[index] == None:
                    self.arr[index] = (key, value)
                    return        
                
        self.arr[h] = (key, value)

    def __getitem__(self, key):
        h = self.get_hash(key)

        if self.arr[h] != None and self.arr[h][0] == key:
            return self.arr[h][1]
        else:
            for i in range(1, self.max):
                index = (h + i) % self.max
                if self.arr[index] != None and self.arr[index][0] == key:
                    return self.arr[index][1]
                
    def __delitem__(self, key):
        h = self.get_hash(key)

        if self.arr[h] != None and self.arr[h][0] == key:
            self.arr[h] = None 
        else:
            for i in range(1, self.max):
                index = (h + i) % 10
                if self.arr[index] != None and self.arr[index][0] == key:
                    self.arr[index] = None 

# Creating an instance of the hashtable
t = hashtable()

# Inserting key-value pairs into the hashtable
t["march 6"] = 20
t["march 17"] = 88
t["march 17"] = 29
t["nov 1"] = 1
t["march 33"] = 234
t["april 2"] = 123

# Deleting a key from the hashtable
del t["april 2"]

# Retrieving and printing values for some keys
print(f"March 17: {t['march 17']}")
print(f"November 1: {t['nov 1']}")
print(f"March 33: {t['march 33']}")
print(f"March 6: {t['march 6']}")