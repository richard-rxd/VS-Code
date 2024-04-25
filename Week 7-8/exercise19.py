class AdultException(Exception):
    def __init__(self):
        self.msg = "Message"
    def print_exeption(self):
        print(self.msg)

class person:
    def __init__(self, age, name):
        self.name = name
        self.age = age
    
    def get_minor_age(self):
        try:
            if self.age < 18:
                print("Minor ", self.age)
                return
            raise AdultException
        except AdultException as x:
            x.print_exeption()
    
    def get_major_age(self):
        try:
            if self.age >= 18:
                print("Major ", self.age)
                return
            raise AdultException
        except AdultException as x:
            x.print_exeption()

p1 = person(18, "Gzuz")
p1.get_minor_age()
p1.get_major_age()